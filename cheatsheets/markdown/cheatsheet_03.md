# Cheatsheet 03: Lists and Dictionaries

## Lists

### Creating a list
```python
my_list = [1, 2, 3, 4, 5]
```

### Accessing elements
```python
first_elem = my_list[0]
last_elem = my_list[-1]
```

### Slicing
```python
sub_list = my_list[1:4]  # Returns [2, 3, 4]
```

### Length of a list
```python
len(my_list)
```

### Adding elements
```python
my_list.append(6)
my_list.extend([7, 8, 9])
```

### Inserting elements
```python
my_list.insert(0, 0)  # Inserts 0 at index 0
```

### Removing elements
```python
my_list.remove(1)  # Removes the first occurrence of 1
item = my_list.pop(1)  # Removes and returns the element at index 1
```

### Sorting
```python
my_list.sort()  # Sorts in ascending order
my_list.sort(reverse=True)  # Sorts in descending order
```

### Reversing
```python
my_list.reverse()
```

### List comprehensions
```python
squares = [x**2 for x in range(1, 6)]  # Returns [1, 4, 9, 16, 25]
```

## Dictionaries

### Creating a dictionary
```python
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
```
### Accessing elements
```python
value = my_dict["key1"]
```

### Accessing elements with `get`
```python
value = my_dict.get("key1")  # Returns None if key doesn't exist
```

### Adding or updating elements
```python
my_dict["key4"] = "value4"
my_dict["key1"] = "new_value1"
```
### Deleting elements
```python
del my_dict["key1"]
```
### Checking if a key exists
```python
if "key1" in my_dict:
    print("Key exists")
```
### Length of a dictionary
```python
len(my_dict)
```

### List of keys
```python
keys = list(my_dict.keys())
```
### List of values
```python
values = list(my_dict.values())
```

### List of key-value pairs (items)
```python
items = list(my_dict.items())
```

### Dictionary comprehensions
```python
squares = {x: x**2 for x in range(1, 6)}  # Returns {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

Remember to replace ```my_list``` and ```my_dict``` with your own list or dictionary variable names.
