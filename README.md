# Steam Inventory Value Calculator
A python script that calculates the total value of a steam user's inventory by using Steam Web API to fetch inventory data and item prices, and displays the results in a Tkinter-based GUI.

**NOTE: Project is still under development.**
- **Results Output:** Currently all results are displayed in the console. Fully developed GUI interface will be implemented in the future.
- **Handling Large Inventories:** Sometimes value calculation could take a very long time especially when dealing with large inventories. That's because a sleep function is being used to prevent excessive requests. Looking for a way to optimize this process.

## Features

- Fetches inventory data from Steam using a profile URL or vanity URL.
- Calculates the total value of marketable items in the inventory.
- Displays detailed information about each item, including name, amount, marketability, and value.
- Provides a simple GUI for user input and output.

## Usage
 1. Obtain a Steam Web API key from https://steamcommunity.com/dev/apikey.
 2. Create config.py file in the project directory.
 3. Set your API key in the config.py file: `api_key = "YOUR_API_KEY"`
 4. Run main.py
 5. Enter your Steam profile URL or vanity URL in the input field and click "Calculate".

## Possible URL inputs
- Vanity URL (for example, `user123`)
- Steam community profile URL (for example, `https://steamcommunity.com/id/user123` or `https://steamcommunity.com/profiles/11122233344455566`)

## How It Works
 1. The user enters a Steam profile URL or vanity URL.
 2. The script extracts the Steam ID from the URL.
 3. It checks if the profile exists and whether it is a custom ID or a numeric ID.
 4. The script resolves the Steam ID to a 64-bit Steam ID if necessary.
 5. It checks the privacy settings of the profile.
 6. If the profile is public, it fetches the inventory data.
 7. The script parses the inventory data and calculates the total value of marketable items.

## Files
- **main.py:** The main script that runs the GUI and handles user input.
- **utils.py:** Contains utility functions for extracting Steam IDs and printing item information.
- **steam_utils.py:** Contains functions for interacting with the Steam Web API and fetching inventory data.
- **config.py:** Contains the API key configuration.

## Console results example
```
------------------------------
Inventory games
------------------------------
Game: Steam, AppID: 753, ContextID: 6
Game: PUBG: BATTLEGROUNDS, AppID: 578080, ContextID: 2
Game: Counter-Strike 2, AppID: 730, ContextID: 2
Game: Team Fortress 2, AppID: 440, ContextID: 2
Game: Valgrave: Immortal Plains, AppID: 1076500, ContextID: 2
Game: Dota 2, AppID: 570, ContextID: 2
Game: Crab Game, AppID: 1782210, ContextID: 2
------------------------------ 

------------------------------
Game: Steam
------------------------------
Item: 730-SWAT, Amount: 1, Marketable: 1, Value: 0.04 €
Item: 2515020-Barnabas, Amount: 2, Marketable: 1, Value: 0.24 €
Item: 2515020-Joshua, Amount: 1, Marketable: 1, Value: 0.12 €
Item: 2515020-Dion, Amount: 1, Marketable: 1, Value: 0.14 €
Item: 2861720-Doze, Amount: 1, Marketable: 1, Value: 0.13 €
Item: 2861720-Cat Hat, Amount: 1, Marketable: 1, Value: 0.13 €
Item: 203160-Turning Point (Profile Background), Amount: 1, Marketable: 0
Item: 874400-First, Amount: 1, Marketable: 0
Item: 1253250-PAX 20th (Profile Background), Amount: 1, Marketable: 0
Item: 1263950-Black Hole, Amount: 1, Marketable: 0
Item: 1462040-Cloud Strife (FINAL FANTASY VII REMAKE INTERGRADE), Amount: 1, Marketable: 0
Item: 2598440-Steam 20th Anniversary, Amount: 1, Marketable: 0
Item: 2598440-Combine Tunak Tunak Tun, Amount: 1, Marketable: 0
Item: 1253250-Big Shot, Amount: 1, Marketable: 0
Item: 1253250-Cool Dude, Amount: 1, Marketable: 0
Item: 1492660-Mafia II Bird, Amount: 1, Marketable: 0
Item: 1846860-Squirrel Nibble, Amount: 1, Marketable: 0
Item: 2575570-Strategy Banners, Amount: 1, Marketable: 0
Item: 2598440-Keyboard Headcrab, Amount: 1, Marketable: 0
Item: 2598440-Day of Disaster, Amount: 1, Marketable: 0
Item: 2598440-Nyan GLaDOS, Amount: 1, Marketable: 0
Item: 2861720-Cat Slippers, Amount: 1, Marketable: 0
Item: 2861720-Snowflake Cookie, Amount: 1, Marketable: 0
Item: 2861720-Stocking, Amount: 1, Marketable: 0
Item: 2861720-String Lights, Amount: 1, Marketable: 0
Item: 2861720-Stuffed Bunny, Amount: 1, Marketable: 0
Item: 2861720-Wreath, Amount: 1, Marketable: 0
Item: 3334340-Best Game You Suck At 2024, Amount: 1, Marketable: 0
Item: 3334340-Best Game on Deck 2024, Amount: 1, Marketable: 0
Item: 3334340-Best Soundtrack 2024, Amount: 1, Marketable: 0
Item: 3334340-Better With Friends 2024, Amount: 1, Marketable: 0
Item: 3334340-Game of the Year 2024, Amount: 1, Marketable: 0
Item: 3334340-Labor of Love 2024, Amount: 1, Marketable: 0
Item: 3334340-Most Innovative Gameplay 2024, Amount: 1, Marketable: 0
Item: 3334340-Outstanding Story-Rich Game 2024, Amount: 1, Marketable: 0
Item: 3334340-Outstanding Visual Style 2024, Amount: 1, Marketable: 0
Item: 3334340-Sit Back and Relax 2024, Amount: 1, Marketable: 0
Item: 3334340-VR Game of the Year 2024, Amount: 1, Marketable: 0
Item: 1239690-Sunset City (Mini Profile Background), Amount: 1, Marketable: 0
Item: 730-Akihabara Accept, Amount: 1, Marketable: 0
Item: 1253250-PAX 20th (Avatar Profile Frame), Amount: 1, Marketable: 0
Item: 1543030-Yue Qingshu Frame, Amount: 1, Marketable: 0
Item: 1732740-Neon Frame, Amount: 1, Marketable: 0
Item: 1629910-Torii (Animated Avatar), Amount: 1, Marketable: 0
Item: 1629910-Cassia (Animated Avatar), Amount: 1, Marketable: 0
Item: 2598440-Counter-Strike... 2, Amount: 1, Marketable: 0
Total items: 47, Total value: 0.8 €
------------------------------

------------------------------
Game: PUBG: BATTLEGROUNDS
------------------------------
Item: SUPPLY LOOT CACHE, Amount: 1, Marketable: 0
Item: BENGAL, Amount: 1, Marketable: 0
Item: Summer Surf - Mini14, Amount: 1, Marketable: 0
Item: Peculiar Greeting, Amount: 1, Marketable: 0
Item: Safari Stripe - UMP, Amount: 1, Marketable: 0
Item: Ready to Rumble Mask, Amount: 1, Marketable: 0
Item: Safari Stripe - S12K, Amount: 1, Marketable: 0
Item: Utility Belt, Amount: 1, Marketable: 0
Item: Hi-top Trainers, Amount: 1, Marketable: 0
Item: Combat Pants (Brown), Amount: 1, Marketable: 0
Item: Combat Pants (Khaki), Amount: 1, Marketable: 0
Item: T-shirt (Gray), Amount: 1, Marketable: 0
Item: T-shirt (White), Amount: 1, Marketable: 0
Item: Survivor-in-Training Hoodie, Amount: 1, Marketable: 0
Item: Ready to Rumble Hat, Amount: 1, Marketable: 0
Item: ARROWHEAD, Amount: 1, Marketable: 0
Total items: 16, Total value: 0 €
------------------------------

------------------------------
Game: Counter-Strike 2
------------------------------
Item: M4A4 | Converter (Field-Tested), Amount: 1, Marketable: 1, Value: 0.46 €
Item: Fracture Case, Amount: 1, Marketable: 1, Value: 0.35 €
Item: SSG 08 | Dezastre (Well-Worn), Amount: 1, Marketable: 1, Value: 0.11 €
Item: Tec-9 | Rebel (Battle-Scarred), Amount: 1, Marketable: 1, Value: 0.08 €
Item: Negev | Bulkhead (Factory New), Amount: 1, Marketable: 1, Value: 0.15 €
Item: MP7 | Army Recon (Factory New), Amount: 1, Marketable: 1, Value: 0.07 €
Item: 5 Year Veteran Coin, Amount: 1, Marketable: 0
Item: Music Kit | Valve, CS:GO, Amount: 1, Marketable: 0
Item: Global Offensive Badge, Amount: 1, Marketable: 0
Item: 2023 Service Medal, Amount: 1, Marketable: 0
Item: AK-47, Amount: 1, Marketable: 0
Total items: 11, Total value: 1.22 €
------------------------------

------------------------------
Game: Team Fortress 2
------------------------------
Item: Mercenary, Amount: 1, Marketable: 0
Item: Abominable Cosmetic Case, Amount: 1, Marketable: 0
Item: Unleash the Beast Cosmetic Case, Amount: 1, Marketable: 0
Total items: 3, Total value: 0 €
------------------------------

------------------------------
Game: Valgrave: Immortal Plains
------------------------------
Item: Alexander the Great, Amount: 1, Marketable: 0
Item: Arthur, Amount: 1, Marketable: 0
Item: Coins, Amount: 40, Marketable: 0
Total items: 42, Total value: 0 €
------------------------------

------------------------------
Game: Dota 2
------------------------------
Item: Armblade of the Chiseled Guard, Amount: 1, Marketable: 0
Item: Gallows Understudy Gauntlets, Amount: 1, Marketable: 0
Item: Dota Plus Victory Shout, Amount: 1, Marketable: 0
Total items: 3, Total value: 0 €
------------------------------

------------------------------
Game: Crab Game
------------------------------
Item: Present, Amount: 1, Marketable: 0
Total items: 1, Total value: 0 €
------------------------------

------------------------------
Total value of whole inventory: 2.02 €
------------------------------
```
