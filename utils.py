from steam_utils import *


def extract_id(entry):
    if entry.startswith('https://steamcommunity.com/id/'):
        entry = entry.replace("https://steamcommunity.com/id/", "")
    elif entry.startswith('https://steamcommunity.com/profiles/'):
        entry = entry.replace("https://steamcommunity.com/profiles/", "")

    return entry


def print_items(steam_id, games, separator):
    total_value = 0

    for game in games:
        print(separator + f'\nGame: {game["name"]}\n' + separator)

        items = get_items(steam_id, game['appid'], game['contextid'])

        if items:
            amount = 0
            value = 0

            for item in items:
                amount += item["amount"]

                if item["marketable"] == 0:
                    print(f'Item: {item["name"]}, Amount: {item["amount"]}, Marketable: {item["marketable"]}')
                else:
                    value += item["value"]

                    print(f'Item: {item["name"]}, Amount: {item["amount"]}, Marketable: {item["marketable"]}, Value: {item["value"]} €')

                total_value += value

            print(f'Total items: {amount}, Total value: {round(value, 2)} €')

            print(separator + '\n')
        else:
            print('No items found.\n' + separator + '\n')

    # print(f'Total value of all items: {round(total_value, 2)} €')
    # print(separator + '\n')
    print(f'{separator}' + '\n' + 'Total value of all items: {round(total_value, 2)} €\n' + separator + '\n')
