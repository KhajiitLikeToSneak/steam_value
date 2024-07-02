from steam_utils import *


def print_items(steam_id, games):
    separator = '-' * 30

    for game in games:
        print(separator + f'\nGame: {game["name"]}\n' + separator)

        items = get_items(steam_id, game['appid'])

        if items:
            amount = 0

            for item in items:
                amount += item["amount"]

                print(f'Item: {item["name"]}, Amount: {item["amount"]}')

            print(f'Total items: {amount}')

            print(separator + '\n')
        else:
            print('No items found.\n' + separator + '\n')
