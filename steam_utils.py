import requests
from bs4 import BeautifulSoup


def get_steamid64(api_key, steam_id):
    response = requests.get(
        f'https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={steam_id}')

    if response.status_code == 200:
        result = response.json()

        if result['response']['success'] == 1:
            return result['response']['steamid']
        else:
            return None
    else:
        print(f'Failed to resolve vanity url {response.status_code}')

def check_privacy(api_key, steam_id):
    response = requests.get(f'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={api_key}&steamids={steam_id}')

    if response.status_code == 200:
        result = response.json()
        privacy = result['response']['players'][0]['communityvisibilitystate']

        if privacy != 3:
            return False
    else:
        print(f'Failed to get player summaries: {response.status_code}')

def fetch_inventory(steam_id, app_id):
    response = requests.get(f'https://steamcommunity.com/inventory/{steam_id}/{app_id}/2?l=english&count=5000')

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch inventory: {response.status_code}')


def get_inventory_html(steam_id):
    response = requests.get(f'https://steamcommunity.com/id/{steam_id}/inventory/')

    if response.status_code == 200:
        return response.text
    else:
        print(f'Failed to fetch inventory page: {response.status_code}')


def parse_inventory_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    games_with_inventory = []
    container = soup.find('div', class_='tabitems_ctn')

    if container:
        game_tabs = container.find_all('a', class_='games_list_tab')

        for tab in game_tabs:
            appid = tab.get('id').split('_')[-1]
            name = tab.find('span', class_='games_list_tab_name').text.strip()

            if appid and name:
                games_with_inventory.append({'appid': appid, 'name': name})
    else:
        return None

    return games_with_inventory


def get_items(steam_id, app_id):
    items = []

    inventory_data = fetch_inventory(steam_id, app_id)

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
                # price = float(get_item_price(app_id, new_item['name']).replace(',', '.').replace('€', ''))

                ### DELETE THIS BLOCK LATER AND UNCOMMENT THE LINE ABOVE
                price = get_item_price(app_id, new_item['name'])
                if price is not None:
                    price = float(price.replace(',', '.').replace('€', ''))
                else:
                    price = 0
                ###

                new_item['value'] = price * int(new_item['amount'])

            items.append(new_item)

    return items


def get_item_price(app_id, market_hash_name):
    response = requests.get(f'https://steamcommunity.com/market/priceoverview/?appid={app_id}&market_hash_name={market_hash_name}&currency={3}')

    if response.status_code == 200:
        result = response.json()

        if result['success'] == 1:
            return result['lowest_price']
        else:
            print(f'Failed to get item price: {result["message"]}')
    else:
        print(f'Failed to get item price: {response.status_code}')
