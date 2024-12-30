import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Dictionary to store contacts
contacts = {}

# Function to load contacts from file
def load_contacts():
    global contacts
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as file:
            contacts = json.load(file)
    else:
        contacts = {}

# Function to save contacts to file
def save_contacts():
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file)

# Function to add a contact
def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    
    # Check if name and phone are entered
    if not name or not phone:
        messagebox.showwarning("Input Error", "Both name and phone number are required.")
        return
    
    # Validate that phone number is numeric
    if not phone.isdigit():
        messagebox.showwarning("Input Error", "Phone number should contain only digits.")
        return

    # Add or update contact
    contacts[name] = phone
    save_contacts()
    update_contact_list()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

# Function to delete a contact
def delete_contact():
    name = name_entry.get().strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_contact_list()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to search for a contact
def search_contact():
    name = name_entry.get().strip()
    if name in contacts:
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contacts[name])
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to update the contact list display
def update_contact_list():
    contact_list_text.delete(1.0, tk.END)
    if not contacts:
        contact_list_text.insert(tk.END, "No contacts to display.")
    else:
        for name, phone in sorted(contacts.items()):
            contact_list_text.insert(tk.END, f"{name}: {phone}\n")

# Set up the main application window
root = tk.Tk()
root.title("Contact Manager")

# Labels and entry fields for adding/searching/deleting contacts
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
name_entry = tk.Entry(root, width=25)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
phone_entry = tk.Entry(root, width=25)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

# Buttons for add, search, and delete functionalities
add_button = tk.Button(root, text="Add Contact", command=add_contact, width=15)
add_button.grid(row=2, column=0, padx=5, pady=5)

search_button = tk.Button(root, text="Search Contact", command=search_contact, width=15)
search_button.grid(row=2, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact, width=15)
delete_button.grid(row=2, column=2, padx=5, pady=5)

# Text widget to display the contact list
contact_list_label = tk.Label(root, text="Contact List:")
contact_list_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5, sticky="w")

contact_list_text = tk.Text(root, height=10, width=50, wrap="none")
contact_list_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Load contacts and initialize contact list display
load_contacts()
update_contact_list()

# Run the application
root.mainloop()