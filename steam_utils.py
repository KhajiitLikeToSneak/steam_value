import json
import re
import time

import requests
from bs4 import BeautifulSoup


def get_steamid64(api_key, steam_id):
    response = requests.get(f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={steam_id}')

    if response.status_code == 200:
        result = response.json()

        if result['response']['success'] == 1:
            return result['response']['steamid']
        else:
            return None
    else:
        print(f'Failed to resolve vanity url {response.status_code}')


def check_profile(steam_id):
    custom_id = None

    response_id = requests.get(f'https://steamcommunity.com/id/{steam_id}')
    response_profiles = requests.get(f'https://steamcommunity.com/profiles/{steam_id}')

    not_found = 'The specified profile could not be found.'
    failed_loading = 'Failed loading profile data, please try again later.'
    if not_found in response_id.text and (not_found in response_profiles.text or failed_loading in response_profiles.text):
        profile_exists = False
    elif not_found not in response_id.text and (not_found in response_profiles.text or failed_loading in response_profiles.text):
        profile_exists = True
        custom_id = True
    else:
        profile_exists = True
        custom_id = False

    return profile_exists, custom_id


def check_privacy(api_key, steam_id):
    response = requests.get(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}')

    if response.status_code == 200:
        result = response.json()
        privacy = result['response']['players'][0]['communityvisibilitystate']

        if privacy != 3:
            return False
    else:
        print(f'Failed to get player summaries: {response.status_code}')


def fetch_inventory(steam_id, app_id, context_id):
    response = requests.get(f'https://steamcommunity.com/inventory/{steam_id}/{app_id}/{context_id}?l=english&count=5000')

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch inventory: {response.status_code}')


def get_inventory_html(steam_id, custom_id):
    if custom_id:
        response = requests.get(f'https://steamcommunity.com/id/{steam_id}/inventory/')
    else:
        response = requests.get(f'https://steamcommunity.com/profiles/{steam_id}/inventory/')

    if response.status_code == 200:
        return response.text
    else:
        print(f'Failed to fetch inventory page: {response.status_code}')


def parse_inventory_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    scripts = soup.find_all('script', type='text/javascript')

    for script in scripts:
        if 'var g_rgAppContextData' in script.text:
            contextdata = re.search('var g_rgAppContextData = (.*?);', script.text).group(1)
            data = json.loads(contextdata)

            if isinstance(data, list):
                return None

            games = []
            for appid, game in data.items():
                for context in game['rgContexts'].values():
                    games.append({
                        'appid': appid,
                        'name': game['name'],
                        'contextid': context['id']
                    })

    return games


def get_items(steam_id, app_id, context_id):
    items = []

    inventory_data = fetch_inventory(steam_id, app_id, context_id)

    if inventory_data:
        assets = {}
        descriptions = inventory_data.get('descriptions', [])

        for item in inventory_data.get('assets', []):
            if item['classid'] in assets:
                assets[item['classid']]['amount'] += int(item['amount'])
            else:
                assets[item['classid']] = item
                assets[item['classid']]['amount'] = int(assets[item['classid']]['amount'])

        for item in descriptions:
            asset = assets.get(item['classid'])
            new_item = ({'name': item.get("market_hash_name"), 'amount': asset.get("amount"), 'marketable': item.get("marketable")})

            if new_item['marketable'] == 1:
                price = float(get_item_price(app_id, new_item['name']).replace(',', '.').replace('€', ''))

                new_item['value'] = price * int(new_item['amount'])

            items.append(new_item)

    return items

def get_item_price(app_id, market_hash_name):
    while True:
        response = requests.get(f'https://steamcommunity.com/market/priceoverview/?appid={app_id}&market_hash_name={market_hash_name}&currency={3}')

        if response.status_code == 200:
            result = response.json()

            if result['success'] == 1:
                return result['lowest_price']
            else:
                print(f'Failed to get item price: {result["message"]}')
                return None
        elif response.status_code == 429:
            print('Too many requests, sleeping for 60 seconds')
            time.sleep(60)
        else:
            print(f'Failed to get item price: {response.status_code}')
            return None