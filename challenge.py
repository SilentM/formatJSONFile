import json
import re


# returns true if any number is contained in the given string
def hasNumbers(input_string):
    return any(char.isdigit() for char in input_string)

# returns max integer present in a string uses regex
def getLargestInteger(string):
    result = re.findall("-?[0-9]+", string)
    return max(map(int, result))


# prompt to enter file name
fileToOpen = input ("Enter name of input JSON file with extension (ex. input.json): ")


# open and read given file
with open(fileToOpen, 'r') as f:
    read_input = json.load(f)


# Assumptions:
# 1) I assumed the data can be nested to any depth so I used a recursive approach.
# 2) For strings in both dictionaries and lists, if it contains numbers, I replace it with the largest integer

# recursive function that walks through json data and removes key/value pairs and replaces values
def recursive_remove_and_replace(data, val_to_remove):
    # checks if object is a dictionary ex. {}
    if isinstance(data, dict):
        # iterate through key/value pair in dictionary
        for key, value in list(data.items()):
            if value in val_to_remove:
                # if value matches one of the values to be removed, delete that key/value pair
                del data[key]
            elif type(value) == str and hasNumbers(value):
                # if value is a string and it contains any digits,
                # replace value with the largest integer value present
                data[key] = getLargestInteger(value)
            elif isinstance(value,(dict, list)):
                # recursively call function if there are nested dictionaries/lists
                recursive_remove_and_replace(value, val_to_remove)
            if value == []:
                # this is to handle case if array becomes empty,
                # then remove the array (ex. [0] -> [] -> removed)
                del data[key]
        # return final modified json string
        return read_input

    # run following if condition when object is a list
    elif isinstance(data, list):
        # iterate through list backwards to make pop operations easier
        # (so we don't run into index out of range runtime errors)
        for index in reversed(range(len(data))):
            if data[index] in val_to_remove:
                # pop value from list if it matches one of the values that need to be removed like 0 for example
                data.pop(index)
            elif type(data[index]) == str and hasNumbers(data[index]):
                # if entry in list is a string and it contains any digits,
                # replace entry with the largest integer value present
                data[index] = getLargestInteger(data[index])
            elif isinstance(data[index], (dict, list)):
                # recursively call function if there are nested dictionaries/lists
                recursive_remove_and_replace(data[index], val_to_remove)
            if len(data) > 0 and data[index] == []:
                # this is to handle the case when nested arrays within arrays become empty.
                # For example,  [[0]] -> [[]] -> [] -> removed
                data.pop(index)


# values to remove from json file. You can modify this array to add more values to remove
valuesToRemove = [0, "", '', {}, []]

# call to the function above to recrusively go through json file and nested structures within.
# Both removing values and replacing strings with greatest integer value.
output_string = recursive_remove_and_replace(read_input, valuesToRemove)


# print modified json string
print(output_string)

# write modified json string to a json file called "output.json" in local directory
with open('output.json', 'w') as out:
    json.dump(output_string, out, indent='\t')

