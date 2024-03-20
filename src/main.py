import tkinter as tk
from tkinter import ttk
import sys
from xlsxReader import *
from itemExtract import *
import Item

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
    # get current menu selection
    global last_menu_selection
    curr_menu_selection = [dropdown_menu.get() for dropdown_menu in dropdown_menus]
    
    for idx_menu_selection in range(0,len(last_menu_selection)-1):
        if curr_menu_selection[idx_menu_selection] != last_menu_selection[idx_menu_selection]:
            for next_menu_selection in range(idx_menu_selection+1,len(last_menu_selection)-1):
                dropdown_menus[next_menu_selection].config(state="disabled")
            break
    
    # Clears the table
    for i in tree.get_children():
        tree.delete(i)

    # refine based on the selection of the first drop-down menu.
    select_type = dropdown_menus[0].get()
    
    
    refined_item = []
    for each_item in extracted_items:
        each_type = each_item[1][1]
        if (each_type == dropdown_menus[0].get()) or (select_type == list(item_types)[0]) \
        or (select_type == list(item_types)[-1] and each_type in type_single_item):
            refined_item.append(each_item)
    
    # get featuer list
    feature_list = []
    try:
        for feature in range(3,len(refined_item[0])-1):
            item = refined_item[0]
            if ":" not in item[feature][1]:
                continue
            feature_label = item[feature][1].split(":",1)[0]
            feature_values = [item[feature][1].split(":",1)[1] for item in refined_item]
            feature_list.append([feature_label,feature_values])
    except:
        ...


    
    for menu_num in range(1,5-1):
        if menu_num > len(feature_list)-1:
            break
        if str(dropdown_menus[menu_num]["state"]) == "disabled":
            feature_label = feature_list[menu_num][0]
            feature_values = feature_list[menu_num][1]
            feature_values.insert(0,f"--{feature_label}--")
            dropdown_menus[menu_num]["values"] = feature_values
            dropdown_menus[menu_num].set(feature_values[0])
            dropdown_menus[menu_num].config(state="enabled")
            
            next_refined_item = []
            for each_item in refined_item:
                each_feature = each_item[3-1+menu_num][1].split(":",1)[1]
                if (each_feature == dropdown_menus[menu_num].get()) or (each_feature == list(item_types)[0]):
                    next_refined_item.append(each_item)
            refined_item = next_refined_item
    
    item_objects = [] # list to be added to the refreshed table in frame 2.
    for each_item in refined_item:
        each_type = each_item[1][1]
        model_number = each_item[2][1]
        details = str(each_item).replace("], [","]\r\n [").replace("None","").replace("[","").replace("]","").replace(",","").replace("'","")
        item_objects.append(Item.Others(each_type,model_number,details))
            
    for item in item_objects:
        tree.insert('', 'end', values=(item.get_type(), item.get_model_number(), 0, item.get_details()))
        
    # save the last selection 
    last_menu_selection = [dropdown_menu.get() for dropdown_menu in dropdown_menus]

# Function to display details of the selected item
def show_details(event):
    selected_item = tree.selection()[0]
    details = tree.item(selected_item, 'values')[3]
    # details_label.config(text=details,anchor='w',justify=tk.LEFT)
    details_label.delete("1.0", "end")
    details_label.insert("1.0",details)

# Function to terminate the entire application
def on_close():
    print("Closing application...")
    root.destroy()  # Destroy the main window
    sys.exit()      # Exit the application

file_path = select_xlsx_file()
if file_path:  # Check if a file was selected
    data_list = read_first_table_to_list(file_path)
else:
    print("No file was selected.")

extracted_items = process_data_list(data_list)

last_menu_selection = ["","","","",""]

# statistics of item types.
item_types = {}
item_types["--item types--"] = -1
for item in extracted_items:
    type = item[1][1]
    if item[1][1] in item_types:
        item_types[type] += 1
    else:
        item_types[type] = 1

# Find keys with the value 1
type_single_item = [key for key, value in item_types.items() if value == 1]
# Create "Others" type
item_types["-Others"] = 0
# Remove single-item type form the item type dictionary.
for typez in type_single_item:
    item_types.pop(typez)
    item_types["-Others"] += 1
    
# Main window
root = tk.Tk()
root.title("Product Selection Tool")

# Handle close GUI window event
root.protocol("WM_DELETE_WINDOW", on_close)  # Bind the close event

# Top frame for dropdowns and search button
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X)

dropdown_menus = []

# the first drop-down list, the type
dropdown = ttk.Combobox(top_frame, values=list(item_types))
dropdown.pack(side=tk.LEFT, padx=10, pady=10)
dropdown.set(list(item_types)[0])
dropdown_menus.append(dropdown)


# Creating the rest 4 dropdown menus with "All" option added (dummie)
dropdown_values = ["", "Category 1", "Category 2", "Category 3", "Category 4", "Category 5"]  # Empty string for 'All'
for i in range(4):
    dropdown = ttk.Combobox(top_frame, values=dropdown_values)
    dropdown.pack(side=tk.LEFT, padx=10, pady=10)
    dropdown.config(state="disabled")
    dropdown_menus.append(dropdown)

search_button = tk.Button(top_frame, text="Search", command=search)
search_button.pack(side=tk.LEFT, padx=10, pady=10)

# Middle frame for displaying search results with a scrollbar
middle_frame = tk.Frame(root)
middle_frame.pack(fill=tk.BOTH, expand=True)

tree_scroll = tk.Scrollbar(middle_frame)
tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(middle_frame, columns=("Type", "Model Number", "Price"), show="headings", yscrollcommand=tree_scroll.set)
tree.heading("Type", text="Type")
tree.heading("Model Number", text="Model Number")
tree.heading("Price", text="Price")
tree.pack(fill=tk.BOTH, expand=True)

tree_scroll.config(command=tree.yview)

tree.bind('<<TreeviewSelect>>', show_details)

# Bottom frame for displaying selected item details
bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X)

details_label = tk.Text(bottom_frame, height=30, width=100)
details_label.delete("1.0", "end")
details_label.insert("1.0","Select an item to see details")
details_label.pack(pady=10,fill='x', padx=10)

root.mainloop()
