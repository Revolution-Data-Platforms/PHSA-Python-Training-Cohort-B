# Cheatsheet 04: Functions and Classes in Python

## Functions

### Defining a function
```python
def function_name(parameters):
    # function body
    return value  # optional
```

### Calling a function
```python
result = function_name(arguments)
```

### Default parameter values
```python
def function_name(param1, param2="default_value"):
    # function body
```

### Lambda functions
```python
lambda_function = lambda parameters: expression
```

### Arbitrary number of arguments (*args)
```python
def function_name(*args):
    # function body
```

### Arbitrary number of keyword arguments (**kwargs)
```python
def function_name(**kwargs):
    # function body
```

## Classes

### Defining a class
```python
class ClassName:
    # class attributes and methods
```

### Class constructor (init method)
```python
class ClassName:
    def __init__(self, parameters):
        self.attributes = values
```

### Creating an object (instance)
```python
object_name = ClassName(arguments)
```

### Accessing object attributes and methods
```python
attribute_value = object_name.attribute
result = object_name.method(arguments)
```
### Class inheritance
```python
class DerivedClass(BaseClass):
    # additional attributes and methods
```
### Calling the base class constructor
```python
class DerivedClass(BaseClass):
    def __init__(self, parameters):
        super().__init__(base_class_parameters)
        # additional attributes
```

### Attribute overriding
```python
class DerivedClass(BaseClass):
    class_attribute = new_value

    def __init__(self, parameters):
        self.instance_attribute = new_value
```

### Method overriding
```python
class DerivedClass(BaseClass):
    def method_name(self, parameters):
        # new method implementation
```
