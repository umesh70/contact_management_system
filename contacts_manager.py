import email
import tkinter as tk
from tkinter import messagebox
import tkinter.font as tkFont
from tkinter import ttk
import csv

class Contact:
    def __init__(self, name, address, phone, email):
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

class contactmanagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Management System")
        self.root.minsize(500,700)
        self.contacts = []

        helv_18 = tkFont.Font(family='Helvetica', size=18)
        helv_14 = tkFont.Font(family='Helvetica', size=14)
        helv_18_bold = tkFont.Font(family='helvetica', size= 24, weight='bold')
        
        self.title_label = tk.Label(root, text="Contact Management System" , font= helv_18_bold)
        self.title_label.grid(row = 0, column=0,columnspan=2, padx = 90, pady=20, sticky = tk.W)

        self.name_label = tk.Label(root, text="Name:", font=helv_18)
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.address_label = tk.Label(root, text="Address:", font=helv_18)
        self.address_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.phone_label = tk.Label(root, text="Phone Number:", font=helv_18)
        self.phone_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
        
        self.email_label = tk.Label(root, text="Email:", font=helv_18)
        self.email_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)

        # Create and place text entry widgets
        self.name_entry = tk.Entry(root, font=helv_18)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)

        self.address_entry = tk.Entry(root, font=helv_18)
        self.address_entry.grid(row=2, column=1, padx=10, pady=5)

        self.phone_entry = tk.Entry(root, font=helv_18)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5)

        self.email_entry = tk.Entry(root, font=helv_18)
        self.email_entry.grid(row=4, column=1, padx=5, pady=5)

        self.add_button = tk.Button(root, text="Add Contact",relief=tk.RAISED, borderwidth=2, bg="#4CAF50", fg="white", activebackground="#45a049", activeforeground="white" ,font=helv_18, command=self.add_contacts)
        self.add_button.grid(row=5, column=0, pady=5)

        # Create and style the View Contacts button
        self.view_button = tk.Button(root, text="View Contacts", font=helv_18, command=self.view_contacts, relief=tk.RAISED, borderwidth=2, bg="#008CBA", fg="white", activebackground="#007EA7", activeforeground="white")
        self.view_button.grid(row=5, column=1, pady=5)

        # Create and style the Search Contact button
        self.search_button = tk.Button(root, text="Search Contact", font=helv_18, command=self.search_contact, relief=tk.RAISED, borderwidth=2, bg="#f44336", fg="white", activebackground="#d32f2f", activeforeground="white")
        self.search_button.grid(row=6, column=0, pady=5)

        self.search_button = tk.Button(root, text="Delete Contact", font=helv_18, command=self.delete_contact, relief=tk.RAISED, borderwidth=2, bg="#f44336", fg="white", activebackground="#d32f2f", activeforeground="white")
        self.search_button.grid(row=6, column=1, pady=5)
        
        self.search_note_label = tk.Label(root, text="*Enter the name to search for a contact:", font=helv_14)
        self.search_note_label.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

    def add_contacts(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and address and phone and email:
            contact = Contact(name, address, phone, email)
            self.contacts.append(contact)
            self.save_contacts()
            self.clear_entries()
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showwarning("Incomplete", "Please fill all fields.")

    def save_contacts(self):
        with open("contacts.csv", "w", newline='', encoding='utf-8') as file:
            fieldnames = ["Name", "Address", "Phone", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({"Name": contact.name, "Address": contact.address, "Phone": contact.phone, "Email": contact.email})

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def view_contacts(self):
        view_window = tk.Toplevel(self.root)
        view_window.title("All Contacts")

        # Create and place Treeview widget to display contacts in a table
        tree = ttk.Treeview(view_window, columns=("Name", "Address", "Phone", "Email"), show="headings")
        tree.heading("Name", text="Name", anchor="center")  # Center-justify the content in the "Name" column
        tree.heading("Address", text="Address")
        tree.heading("Phone", text="Phone Number")
        tree.heading("Email", text="Email Address")
        tree.pack(padx=10, pady=10)

        # Load contacts from CSV file and add to Treeview
        self.load_contacts()
        for contact in self.contacts:
            tree.insert("", "end", values=(contact.name, contact.address, contact.phone, contact.email))

    def load_contacts(self):
        self.contacts.clear()  # Clear the existing contacts before loading from CSV
        try:
            with open("contacts.csv", newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    contact = Contact(row["Name"], row["Address"], row["Phone"], row["Email"])
                    self.contacts.append(contact)
        except FileNotFoundError:
            pass
    
    def search_contact(self):
        search_name = self.name_entry.get()
        if search_name:
            found_contacts = [contact for contact in self.contacts if contact.name.lower() == search_name.lower()]

            if found_contacts:
                search_window = tk.Toplevel(self.root)
                search_window.title("Search Results")

                # Create and place Treeview widget to display search results in a table
                tree = ttk.Treeview(search_window, columns=("Name", "Address", "Phone", "Email"), show="headings")
                tree.heading("Name", text="Name", anchor="center")  # Center-justify the content in the "Name" column
                tree.heading("Address", text="Address")
                tree.heading("Phone", text="Phone Number")
                tree.heading("Email", text="Email Address")
                tree.pack(padx=10, pady=10)

                # Add search results to the Treeview
                for contact in found_contacts:
                    tree.insert("", "end", values=(contact.name, contact.address, contact.phone, contact.email))
            else:
                messagebox.showinfo("Not Found", f"No contact found with name: {search_name}")
        else:
            messagebox.showwarning("Empty Search", "Please enter a name to search.")

    def delete_contact(self):
       delete_name = self.name_entry.get()
       if delete_name:
           deleted_contact = None
           for contact in self.contacts:
               if contact.name.lower() == delete_name.lower():
                   deleted_contact = contact
                   self.contacts.remove(contact)
                   self.save_contacts()  # Save the updated contacts to the CSV file
                   break

           if deleted_contact:
               messagebox.showinfo("Deleted", f"Contact {delete_name} has been deleted.")
               self.view_contacts()  # Update the table view
               self.clear_entries()
           else:
               messagebox.showinfo("Not Found", f"No contact found with name: {delete_name}")
       else:
           messagebox.showwarning("Empty Input", "Please enter a name to delete.")

    def save_contacts(self):
        with open("contacts.csv", "w", newline='', encoding='utf-8') as file:
            fieldnames = ["Name", "Address", "Phone", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({"Name": contact.name, "Address": contact.address, "Phone": contact.phone, "Email": contact.email})
if __name__ == "__main__":
    root = tk.Tk()
    app = contactmanagement(root)
    root.mainloop()