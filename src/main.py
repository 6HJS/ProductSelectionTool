import tkinter as tk
from tkinter import ttk
from xlsxReader import *
from itemExtract import *

# Sample data with 10 items
data = [
    {"name": "Item 1", "category": "Category 1", "price": "100", "details": "Details of Item 1"},
    {"name": "Item 2", "category": "Category 1", "price": "150", "details": "Details of Item 2"},
    {"name": "Item 3", "category": "Category 2", "price": "200", "details": "Details of Item 3"},
    {"name": "Item 4", "category": "Category 2", "price": "250", "details": "Details of Item 4"},
    {"name": "Item 5", "category": "Category 3", "price": "300", "details": "Details of Item 5"},
    {"name": "Item 6", "category": "Category 3", "price": "350", "details": "Details of Item 6"},
    {"name": "Item 7", "category": "Category 4", "price": "400", "details": "Details of Item 7"},
    {"name": "Item 8", "category": "Category 4", "price": "450", "details": "Details of Item 8"},
    {"name": "Item 9", "category": "Category 5", "price": "500", "details": "Details of Item 9"},
    {"name": "Item 10", "category": "Category 5", "price": "550", "details": "Details of Item 10"},
]

# Search function that filters data based on the first dropdown selection
def search():
    # Clears the table
    for i in tree.get_children():
        tree.delete(i)

    selected_category = dropdown_menus[0].get()  # Assuming filtering by the first dropdown
    filtered_data = [item for item in data if item['category'] == selected_category or selected_category == ""]

    # Repopulates it with filtered data
    for item in filtered_data:
        tree.insert('', 'end', values=(item['name'], item['category'], item['price'], item['details']))

# Function to display details of the selected item
def show_details(event):
    selected_item = tree.selection()[0]
    details = tree.item(selected_item, 'values')[3]
    details_label.config(text=details)

file_path = select_xlsx_file()
if file_path:  # Check if a file was selected
    data_list = read_first_table_to_list(file_path)
else:
    print("No file was selected.")

extracted_items = process_data_list(data_list)

# Main window
root = tk.Tk()
root.title("Product Selection Tool")

# Top frame for dropdowns and search button
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X)

# Creating 5 dropdown menus with "All" option added
dropdown_values = ["", "Category 1", "Category 2", "Category 3", "Category 4", "Category 5"]  # Empty string for 'All'
dropdown_menus = []
for i in range(5):
    dropdown = ttk.Combobox(top_frame, values=dropdown_values)
    dropdown.pack(side=tk.LEFT, padx=10, pady=10)
    dropdown_menus.append(dropdown)

search_button = tk.Button(top_frame, text="Search", command=search)
search_button.pack(side=tk.LEFT, padx=10, pady=10)

# Middle frame for displaying search results with a scrollbar
middle_frame = tk.Frame(root)
middle_frame.pack(fill=tk.BOTH, expand=True)

tree_scroll = tk.Scrollbar(middle_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(middle_frame, columns=("Name", "Category", "Price"), show="headings", yscrollcommand=tree_scroll.set)
tree.heading("Name", text="Name")
tree.heading("Category", text="Category")
tree.heading("Price", text="Price")
tree.pack(fill=tk.BOTH, expand=True)

tree_scroll.config(command=tree.yview)

tree.bind('<<TreeviewSelect>>', show_details)

# Bottom frame for displaying selected item details
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X)

details_label = tk.Label(bottom_frame, text="Select an item to see details")
details_label.pack(pady=10)

root.mainloop()
