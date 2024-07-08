def extract_id(entry):
    if entry.startswith('https://steamcommunity.com/id/'):
        entry = entry.replace("https://steamcommunity.com/id/", "")

    return entry
