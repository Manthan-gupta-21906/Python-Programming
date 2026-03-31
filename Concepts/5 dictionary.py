# Dictionary ek key-value pair ka collection hota hai
# - Ordered (Python 3.7+)
# - Mutable (change ho sakta hai)
# - No duplicate keys allowed

print("==========================Creating a Dictionary===================================")

# Method 1: Curly braces se
student = {
    "name": "Manthan",
    "course": "Btech (Mathematics and Computing)",
    "entry_no": "25bcm028",
    "year": 1
}
print(student)
print(type(student))

# Method 2: dict() constructor se
student2 = dict(name="Rahul", course="CSE", year=2)
print(student2)

# Method 3: Empty dictionary
empty_dict = {}
print(empty_dict)

print("==========================Accessing Values===================================")

# Method 1: Square bracket []
print(student["name"])
print(student["course"])

# Method 2: .get() - safe way (KeyError nahi aayega agar key nahi hai)
print(student.get("year"))
print(student.get("cgpa"))           # None return karta hai
print(student.get("cgpa", "N/A"))    # Default value de sakte ho

print("==========================Updating / Adding Values===================================")

student["cgpa"] = 9.2                   # Naya key add kiya
print(student)

student["cgpa"] = 9.5                   # Existing key update kiya
print(student)

# .update() se ek saath kai values update/add karo
student.update({"city": "Katra", "year": 2})
print(student)

print("==========================Removing Values===================================")

# .pop() - key specify karke remove karo, value return karta hai
removed = student.pop("city")
print("Removed:", removed)
print(student)

# .popitem() - last inserted item remove karta hai (Python 3.7+)
last = student.popitem()
print("Last item removed:", last)
print(student)

# del keyword
del student["cgpa"]
print(student)

# .clear() - saari dict khaali kar do
temp = {"a": 1, "b": 2}
temp.clear()
print("After clear:", temp)

print("==========================Useful Dictionary Methods===================================")

data = {
    "name": "Manthan",
    "course": "Btech",
    "year": 1,
    "city": "Srinagar"
}

# .keys() - saari keys milti hain
print(data.keys())

# .values() - saari values milti hain
print(data.values())

# .items() - saare key-value pairs as tuples
print(data.items())

# len() - kitne pairs hain
print("Length:", len(data))

print("==========================Checking if Key Exists===================================")

print("name" in data)          # True
print("cgpa" in data)          # False
print("cgpa" not in data)      # True

# Using if
if "year" in data:
    print("Year hai:", data["year"])

print("==========================Looping through Dictionary===================================")

# Sirf keys
for key in data:
    print(key)

# Keys aur values dono
for key, value in data.items():
    print(f"{key} --> {value}")

# Sirf values
for value in data.values():
    print(value)

print("==========================Nested Dictionary===================================")

# Dictionary ke andar dictionary
college = {
    "student1": {
        "name": "Manthan",
        "year": 1
    },
    "student2": {
        "name": "Rahul",
        "year": 2
    }
}

print(college)
print(college["student1"]["name"])   # Nested access

# Loop karo nested dict mein
for student_id, info in college.items():
    print(f"\n{student_id}:")
    for key, value in info.items():
        print(f"  {key}: {value}")

print("==========================Dictionary Comprehension===================================")

# Syntax: {key: value for item in iterable}

# Example 1: Squares ki dict
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# Example 2: Sirf even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)

# Example 3: String ki length dict
words = ["Manthan", "Python", "SMVDU"]
word_lengths = {word: len(word) for word in words}
print(word_lengths)

print("==========================Copying a Dictionary===================================")

original = {"a": 1, "b": 2}

# Shallow copy - .copy()
copy1 = original.copy()
copy1["a"] = 99
print("Original:", original)    # Original unchanged
print("Copy:", copy1)

# dict() se bhi copy hoti hai
copy2 = dict(original)
print("Copy2:", copy2)

# NOTE: Deep nested dict ke liye import copy aur use copy.deepcopy()

print("==========================.fromkeys() Method===================================")

# Ek hi default value se nayi dict banao
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)

print("==========================.setdefault() Method===================================")

# Agar key nahi hai toh add karo, agar hai toh kuch mat karo
info = {"name": "Manthan"}
info.setdefault("name", "Default")    # Key already hai, kuch nahi hoga
info.setdefault("cgpa", 0.0)          # Key nahi thi, add ho gayi
print(info)

print("==========================Merging Two Dictionaries===================================")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: .update()
dict1.update(dict2)
print("Merged:", dict1)

# Method 2: ** unpacking (Python 3.5+)
merged = {**dict1, **dict2}
print("Merged with **:", merged)

# Method 3: | operator (Python 3.9+)
merged2 = dict1 | dict2
print("Merged with |:", merged2)

print("==========================Type Flexibility in Dictionary===================================")

# Keys aur values kuch bhi ho sakti hain (keys: immutable types only)
flexible = {
    "string_key": "value",
    42: "integer key",
    (1, 2): "tuple key",       # Tuple key ho sakti hai (immutable)
    "list_value": [1, 2, 3],   # Value mutable bhi ho sakti hai
    "dict_value": {"nested": True}
}
print(flexible)

# List key nahi ho sakti (mutable) - yeh ERROR dega:
# bad = {[1,2]: "value"}  # typeError
