"""
main.py
Main entry point for running the contact manager app.
"""

from contacts_manager import ContactsManager


def main():
    """Run the contact manager menu loop."""
    manager = ContactsManager()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Show All Contacts")
        print("4. Backup Contacts")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            manager.add(name, number)
            print("Contact added!")

        elif choice == "2":
            name = input("Enter name to search: ")
            manager.search(name)

        elif choice == "3":
            manager.show_contacts()

        elif choice == "4":
            manager.backup()
            print("Contacts backed up to contacts_list.json")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
