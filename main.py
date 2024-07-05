from steam_utils import *
import tkinter as tk

api_key = 'B27C5FCB7D3D0F6E7B9DC78A7AE05EFB'
separator = '-' * 30


def on_submit():
    profile_url = entry.get()

    steam_id = profile_url.split('/')[-1]
    # print(steam_id)
    steam_id_64 = get_steamid64(api_key, steam_id)

    print(separator + f'\nSteamID64: {steam_id_64}\n' + separator + '\n')

    html_content = get_inventory_html(steam_id)
    inventory_games = parse_inventory_html(html_content)

    print(separator + f'\nInventory games\n' + separator)

    for game in inventory_games:
        print(f'Game: {game["name"]}, AppID: {game["appid"]}')

    print(f'-' * 30 + f' \n')

    print_items(steam_id_64, inventory_games, separator)


def print_items(steam_id, games, separator):
    for game in games:
        print(separator + f'\nGame: {game["name"]}\n' + separator)

        items = get_items(steam_id, game['appid'])

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

            print(f'Total items: {amount}, Total value: {round(value, 2)} €')

            print(separator + '\n')
        else:
            print('No items found.\n' + separator + '\n')


root = tk.Tk()
root.minsize(500, 350)
root.configure(background='gray')

label = tk.Label(root, text="Enter your steam profile URL: ")  # https://steamcommunity.com/id/gedl333
label.pack(pady=20)

entry = tk.Entry(root, width=50, borderwidth=3)
entry.pack()

button = tk.Button(root, text="Calculate", command=on_submit)
button.pack(pady=10)

root.mainloop()
