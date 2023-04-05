# Cheatsheet 02: Conditional Statements and Loops

## Conditional Statements

### `if` Statements


```python
if condition:
    statement(x)
```

### `if-else` Statements


```python
if condition:
    statement(x)  # executes if condition is True
else:
    statement(y)  # executes if condition is False
```

### `if-elif-else` Statements


```python
if condition1:
    statement(x)  # executes if condition1 is True
elif condition2:
    statement(y)  # executes if condition1 is False and condition2 is True
else:
    statement(z)  # executes if all conditions are False
```

## Loops

### `for` Loops


```python
for variable in iterable:
    statement(s)
```

#### `range()` Function


```python
range(stop)         # generates a sequence from 0 to stop-1
range(start, stop)  # generates a sequence from start to stop-1
range(start, stop, step)  # generates a sequence from start to stop-1 with a specified step
```

#### `for` Loop with `range()` Function


```python
for i in range(start, stop, step):
    statement(s)
```

#### `for` Loop with `enumerate()` Function


```python
for index, value in enumerate(iterable, start=0):
    statement(s)
```

### `while` Loops


```python
while condition:
    statement(s)
```

### `break` Statement


```python
# Terminates the loop and exits immediately
if condition:
    break
```

### `continue` Statement


```python
# Skips the rest of the loop's body and continues with the next iteration
if condition:
    continue
```

### `pass` Statement


```python
# Acts as a placeholder and does nothing, allowing an empty code block
if condition:
    pass
```

### Nested Loops 


```python
for outer_variable in outer_iterable:
    for inner_variable in inner_iterable:
        statement(s)
```
