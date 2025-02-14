from utils import *
from steam_utils import *
import tkinter as tk
import config

separator = '-' * 30


def on_submit():
    profile_url = entry.get()
    steam_id = extract_id(profile_url)

    profile_exists, custom_id = check_profile(steam_id)

    if not profile_exists:
        print('Profile not found.')
        return

    if custom_id:
        steam_id_64 = get_steamid64(config.api_key, steam_id)
    else:
        steam_id_64 = steam_id

    if check_privacy(config.api_key, steam_id_64) is False:
        print('Profile is private.')
        return

    html_content = get_inventory_html(steam_id, custom_id)
    inventory_games = parse_inventory_html(html_content)

    if inventory_games is None:
        print('Inventory is private.')
        return

    print(separator + f'\nInventory games\n' + separator)

    for game in inventory_games:
        print(f'Game: {game["name"]}, AppID: {game["appid"]}, ContextID: {game["contextid"]}')

    print(f'-' * 30 + f' \n')

    print_items(steam_id_64, inventory_games, separator)


root = tk.Tk()
root.minsize(500, 350)
root.configure(background='gray')

label = tk.Label(root, text="Enter your steam profile URL: ")
label.pack(pady=20)

entry = tk.Entry(root, width=50, borderwidth=3)
entry.pack()

button = tk.Button(root, text="Calculate", command=on_submit)
button.pack(pady=10)

root.mainloop()
