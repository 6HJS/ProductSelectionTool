import re

# Function to filter out sub-lists based on a keyword in the first string
def filter_sublists(sublists, keyword):
    # return [sublist for sublist in sublists if keyword not in sublist[0]]
    new_sublists = []
    for sublist in sublists:
        if sublist[0] is not None:
            if keyword not in sublist[0]:
                new_sublists.append(sublist)
        elif sublist[1] is not None:
            new_sublists.append(sublist)
    return new_sublists


# Regular expression to match the specific pattern in the first column
pattern = r'^\d{18}\s{22}\d{6}$'

# Function to process the data_list and extract relevant rows based on the pattern
def process_data_list(data_list):
    extracted_data = []
    current_chunk = []
    collecting = False  # Flag to start collecting data after the first match

    for row in data_list:
        # Check if the first column is not None and matches the pattern
        if (row[0] is not None) and (re.match(pattern, row[0])):
            if collecting:
                # Using the function to filter out sub-lists containing "SAP" in the first string
                current_chunk = filter_sublists(current_chunk, "SAP")
                # If already collecting, it means a new pattern has started, save the current_chunk
                extracted_data.append(current_chunk)
                current_chunk = []
            else:
                # Start collecting data from now on
                collecting = True
            # Include the matching row in the new chunk as per updated requirement
            current_chunk.append(row[:2])
        elif collecting:
            # If the row doesn't match the pattern but collecting has started, include it
            current_chunk.append(row[:2])

    # Add the last chunk if collecting has started and it hasn't been added yet
    if collecting and current_chunk:
        extracted_data.append(current_chunk)
        
    return extracted_data

if __name__ == "__main__":
    # Example 'data_list' for demonstration. Replace with actual data loading or selection logic.
    data_list = [
        ["Should be ignored before match", "Row0Col2"],
        ["000000000000000001                      000001", "Row1Col2"],
        ["Data after first match", "Row2Col2"],
        ["000000000000000002                      000002", "Row3Col2"],
        ["Data between patterns", "Row4Col2"],
        ["123456789012345678                      123456", "Data not matching pattern", "Row5Col3"],
        ["Another row to ignore", "Row6Col2"],
        ["000000000000000003                      000003", "Row7Col2"],
        ["Data after last match", "Row8Col2"]
    ]

    extracted_data = process_data_list(data_list)

    # Print the extracted data for verification
    for chunk in extracted_data:
        print(chunk)
