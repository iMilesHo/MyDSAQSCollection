# Dictionary

- A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
- Dictionaries are used to store data values in key:value pairs.

## Creating a Dictionary

- Dictionaries are written with curly brackets, and they have keys and values.

```python
# initialize dictionary
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_dict = dict(brand="Ford", model="Mustang", year=1964)]
my_dict = dict([("brand", "Ford"), ("model", "Mustang"), ("year", 1964)])

# empty dictionary
my_dict = {}
my_dict = dict()
```

## Accessing Items

- You can access the items of a dictionary by referring to its key name, inside square brackets:

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(my_dict["brand"])  # Output: Ford
print(my_dict.get("model"))  # Output: Mustang

# if the key does not exist, it will raise an error
print(my_dict["price"])  # KeyError: 'price'

# if the key does not exist, it will return None
print(my_dict.get("price"))  # Output: None
```

## Changing Items

- You can change the value of a specific item by referring to its key name:

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_dict["year"] = 2018
print(my_dict)  # Output: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

# if the key does not exist, it will add a new key-value pair
my_dict["color"] = "red"

# if the key exists, it will change the value
my_dict["color"] = "blue"

# or
my_dict.update({"color": "red"}) # if the key exists, it will change the value, if not, it will add a new key-value pair
```

## Removing Items

- You can remove a specific item in a dictionary by using the pop() method. This method removes an item with the provided key and returns the value.

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_dict.pop("model")
print(my_dict)  # Output: {'brand': 'Ford', 'year': 1964}

# if the key does not exist, it will raise an error
my_dict.pop("price")  # KeyError: 'price'

# then, we can use other methods to remove an item to avoid the error
my_dict.pop("price", None)  # if the key does not exist, it will return None

# or
del my_dict["model"]
```

## Loop Through a Dictionary

- You can loop through a dictionary by using a for loop.

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for key in my_dict:
  print(key)  # Output: brand, model, year

# or
for key in my_dict.keys():
  print(key)  # Output: brand, model, year

# or
for value in my_dict.values():
  print(value)  # Output: Ford, Mustang, 1964

# or
for key, value in my_dict.items():
  print(key, value)  # Output: brand Ford, model Mustang, year 1964
```

## Copy a Dictionary

- You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
- There are ways to make a copy, one way is to use the built-in Dictionary method copy().

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

my_dict2 = my_dict.copy()
```

## sort the dictionary

- You can sort the dictionary by using the sorted() function.

```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# sort by key
sorted_dict = dict(sorted(my_dict.items()))

# sort by value
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
```
