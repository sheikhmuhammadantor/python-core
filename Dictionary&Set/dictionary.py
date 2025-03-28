# Dictionary Like JavaScript Object;
# Dictionary:
student = {
    "name" : "Muhammad",
    "subject": {
        "phy" : 97,
        "chy" : 98,
    }
}

print(len(list(student.keys())));
print(student["name"])
print(student.get("name")) # Not throw an error if key doesn't exit;

# Methods:
"""
Dict.keys() # returns all keys;
Dict.values() # returns all values;
Dict.items() # returns all (key, val) pairs as tuples, List of Tuples;
Dict.get("key"); # returns the value according to key;
Dict.update(new_dict) # inserts the specified items to the dictionary;
"""
