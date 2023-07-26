# contact_management_system

The project is a simple Contact Management System implemented using Python's `tkinter` library for the GUI functionality.
The goal of the project is to allow users to store, manage, view, search, and delete contacts.
The project is organized using classes, with each contact represented as an instance of the `Contact` class.

To install tkinkter simply run ```pip install tk``` in command prompt
and to import tkinkter in your projects simply add ```import tkinkter as ttk``` or ```import tkinkter ```

Here's a description of the project's functionality and key components:

1. `Contact` Class:
   - This class represents a single contact and stores its attributes, such as name, address, phone number, and email.
   - Each contact is an instance of this class, and we use it to encapsulate contact data.

2. `ContactManagementApp` Class:
   - This class is responsible for the main application window and GUI functionality.
   - It creates the main application window using `tkinter`.
   - The class contains various labels, entry widgets, and buttons for users to interact with and manage contacts.

3. Add Contact:
   - Users can enter a new contact's information, such as name, address, phone number, and email, into the respective entry widgets.
   - The "Add Contact" button allows users to save the contact by creating a new instance of the `Contact` class and appending it to the `self.contacts` list.
   - The new contact is also stored in a CSV file for persistence.

4. View Contacts:
   - The "View Contacts" button opens a new window that displays all saved contacts in a table-like format.
   - The contacts are fetched from the CSV file using the `load_contacts` method and displayed using a `ttk.Treeview` widget for a structured view.

5. Search Contact:
   - Users can search for a contact by entering the name in the search entry widget.
   - The "Search Contact" button initiates the search, and the matching contact(s) are displayed in a new window, similar to the "View Contacts" functionality.

6. Delete Contact:
   - Users can delete a contact by entering the name in the delete entry widget and clicking the "Delete Contact" button.
   - The specified contact is removed from the `self.contacts` list and the CSV file using the `delete_contact` method.

7. CSV File Handling:
   - The contact information is stored in a CSV file named "contacts.csv" for persistence between program runs.
   - When the program starts, it reads the existing contacts from the CSV file and populates the `self.contacts` list.
   - Contacts added, deleted, or modified during the session are saved back to the CSV file using the `save_contacts` method.

8. Styling and GUI Layout:
   - The GUI is designed using `tkinter` widgets such as `Label`, `Entry`, `Button`, and `ttk.Treeview`.
   - Fonts and styling are applied to improve the appearance of the application.
   - The main window and additional windows are created using `Toplevel`.

I was such a nice experience working on this, I was able to get hands on experience to implement GUI functionalities in python.
