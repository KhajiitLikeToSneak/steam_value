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
 3. Set your API key in the config.py file: api_key = "YOUR_API_KEY"
 4. Run main.py
 5. Enter your Steam profile URL or vanity URL in the input field and click "Calculate".

## Possible URL inputs:
- Vanity URL (for example, `rxgucci`)
- Steam community profile URL (for example, `https://steamcommunity.com/id/rxgucci` or `https://steamcommunity.com/profiles/76561198216779888`)

## How It Works
 1. The user enters a Steam profile URL or vanity URL.
 2. The script extracts the Steam ID from the URL.
 3. It checks if the profile exists and whether it is a custom ID or a numeric ID.
 4. The script resolves the Steam ID to a 64-bit Steam ID if necessary.
 5. It checks the privacy settings of the profile.
 6. If the profile is public, it fetches the inventory data.
 7. The script parses the inventory data and calculates the total value of marketable items.

## Files
- main.py: The main script that runs the GUI and handles user input.
- utils.py: Contains utility functions for extracting Steam IDs and printing item information.
- steam_utils.py: Contains functions for interacting with the Steam Web API and fetching inventory data.
- config.py: Contains the API key configuration.