"""
contacts_manager.py
Simple contact manager with add, search, show, and backup features.
"""

import json


class ContactsManager:
    """Manage contacts list with add, search, show, and backup."""

    def __init__(self, path="-"):
        """Initialize contact list, optionally load from JSON file."""
        self.contact_list = []

        if path != "-":
            print("Loading previous contacts ...")
            with open(path, "r", encoding="utf-8") as file:
                data = file.read()
                self.contact_list = json.loads(data)
            print("Loaded ...")

    def add(self, name, number):
        """Add a new contact with name and number."""
        self.contact_list.append({"Name": name, "Number": number})

    def search(self, name):
        """Search contacts by name (case-insensitive)."""
        result = []
        for item in self.contact_list:
            if name.lower() in item["Name"].lower():
                result.append(item)
        print(result)

    def backup(self):
        """Save contacts to contacts_list.json as JSON."""
        with open("./contacts_list.json", "w", encoding="utf-8") as file:
            file.write(json.dumps(self.contact_list, indent=3, ensure_ascii=False))

    def show_contacts(self):
        """Print all contacts."""
        print(self.contact_list)
