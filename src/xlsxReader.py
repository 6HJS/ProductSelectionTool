import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np

def select_xlsx_file(default_directory='./data/'):
    root = tk.Tk()
    root.withdraw()  # We don't want a full GUI, so keep the root window from appearing
    file_path = filedialog.askopenfilename(initialdir=default_directory,
                                           title="Select file",
                                           filetypes=(("Excel files", "*.xlsx"), ("All files", "*.*")))
    return file_path

def read_first_table_to_list(file_path):
    # Load the workbook
    xls = pd.ExcelFile(file_path)
    # Load the first sheet into a DataFrame
    df = pd.read_excel(xls, sheet_name=xls.sheet_names[0])
    
    # Attempt to identify the start of the table based on the first non-empty row and column
    # This assumes the table starts where the first non-empty cell is found
    first_row = df.dropna(how='all').index[0]  # First non-empty row
    first_col = df.dropna(axis=1, how='all').columns[0]  # First non-empty column
    
    # Assuming the table is contiguous, slice the DataFrame from the first non-empty cell
    table_df = df.loc[first_row:, first_col:]
    
    # Remove any entirely empty rows or columns that might be within the table
    table_df = table_df.dropna(how='all').dropna(axis=1, how='all')
    
    # Convert to 2-D list, handling NaN values by converting them to None or another placeholder
    data_list = table_df.where(pd.notnull(table_df), None).values.tolist()
    
    return data_list
if __name__ == "__main__":
    # Main workflow
    file_path = select_xlsx_file()
    if file_path:  # Check if a file was selected
        data_list = read_first_table_to_list(file_path)
        print(data_list)
    else:
        print("No file was selected.")
