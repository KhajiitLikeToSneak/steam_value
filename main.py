from steam_utils import *
from data_utils import print_items

api_key = 'B27C5FCB7D3D0F6E7B9DC78A7AE05EFB'
steam_id = 'gedl333'

separator = '-' * 30

steam_id_64 = get_steamid64(api_key, steam_id)

print(separator + f'\nSteamID64: {steam_id_64}\n' + separator + '\n')

html_content = get_inventory_html(steam_id)
inventory_games = parse_inventory_html(html_content)

print(separator + f'\nInventory games\n' + separator)

for game in inventory_games:
    print(f'Game: {game["name"]}, AppID: {game["appid"]}')

print(f'-' * 30 + f' \n')

print_items(steam_id_64, inventory_games)
