from fuzzywuzzy import fuzz

# Define two strings
string1 = "Switching output: Push-pull: PNP/NPN"
string2 = input("Input a string: ")

# Calculate fuzzy ratio
ratio = fuzz.ratio(string1.lower(), string2.lower())

print(f"Fuzzy Ratio: {ratio}")
