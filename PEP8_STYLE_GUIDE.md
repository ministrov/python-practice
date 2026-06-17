# PEP 8 Style Guide for This Repository

This document summarizes the PEP 8 conventions that must be followed in all code within this repository. It serves as a quick reference for consistent, readable Python code.

**Source:** https://peps.python.org/pep-0008/

## Code Layout & Indentation

- **Indentation:** 4 spaces per level, never tabs
- **Line length:** Maximum 79 characters (72 for comments and docstrings)
- **Blank lines:** 
  - 2 blank lines between top-level functions and classes
  - 1 blank line between methods in a class
  - Use blank lines inside functions sparingly to separate logical sections

## Naming Conventions (CRITICAL)

| Element | Convention | Example |
|---------|-----------|---------|
| **Functions** | lowercase_with_underscores | `calculate_age()`, `fetch_user()` |
| **Variables** | lowercase_with_underscores | `user_name`, `total_price` |
| **Constants** | ALL_CAPS_WITH_UNDERSCORES | `MAX_RETRIES`, `DEFAULT_TIMEOUT` |
| **Classes** | CapitalWords (PascalCase) | `UserAccount`, `DatabaseConnection` |
| **Private** | _single_leading_underscore | `_internal_method`, `_cache_data` |
| **Dunder** | __double_underscores__ | `__init__`, `__str__` |

### Naming Anti-patterns
❌ Avoid using single-character names that look like numbers:
- `l` (lowercase L) — looks like 1
- `O` (capital O) — looks like 0
- `I` (capital i) — looks like 1

## Imports

```python
# Correct order and grouping:
import os
import sys
from datetime import datetime

import requests
import numpy as np

from my_package import helper
from .local_module import utility
```

**Rules:**
- Place imports at the top of the file, after docstrings
- Three groups separated by blank lines:
  1. Standard library imports
  2. Third-party imports
  3. Local application imports
- Use absolute imports when possible
- Avoid `from module import *` (wildcard imports)
- One import per line (except `from x import a, b` is ok)

## Whitespace

### Around Operators
```python
# ✅ Correct
x = 1
if x == 2:
    y = x + 1

# ❌ Incorrect
x=1
if x==2:
    y=x+1
```

### Inside Parentheses & Brackets
```python
# ✅ Correct
func(arg1, arg2)
list_items = [1, 2, 3]
dict_items = {"key": "value"}

# ❌ Incorrect
func( arg1 , arg2 )
list_items = [ 1 , 2 , 3 ]
dict_items = { "key" : "value" }
```

### Function Arguments
```python
# ✅ Correct — no spaces around = in keyword arguments
func(arg1, arg2, timeout=30)

# ❌ Incorrect
func(arg1, arg2, timeout = 30)
```

### Slicing
```python
# ✅ Correct
x[1:2]
x[1:2:3]  # extended slice: spaces around colons

# ❌ Incorrect
x[ 1 : 2 ]
```

## Comments and Docstrings

### Inline Comments
```python
# ✅ Correct — clarifies non-obvious code
x = x + 1  # Compensate for border offset

# ❌ Incorrect — obvious, wastes space
x = x + 1  # Increment x
```

### Block Comments
```python
# ✅ Correct — complete sentences, capitalized
# This is a complex algorithm that requires
# multiple iterations to converge.

# ❌ Incorrect
# does complex stuff
# iterates a bunch
```

### Docstrings
```python
def fetch_user(user_id):
    """Fetch a user by ID from the database.
    
    Args:
        user_id: Integer ID of the user.
    
    Returns:
        User object if found, None otherwise.
    
    Raises:
        DatabaseError: If connection fails.
    """
    # implementation here
```

**Rules:**
- All public modules, functions, classes, and methods must have docstrings
- Single-line docstrings fit on one line
- Multi-line docstrings: opening `"""` on first line, body, closing `"""` on own line
- Use imperative mood ("Fetch" not "Fetches")

## Programming Recommendations

### Type Checking
```python
# ✅ Correct
if isinstance(x, int):
    pass

# ❌ Incorrect
if type(x) == int:
    pass
```

### Comparing to None
```python
# ✅ Correct
if x is None:
    pass
if x is not None:
    pass

# ❌ Incorrect
if x == None:
    pass
if x != None:
    pass
```

### String Operations
```python
# ✅ Correct — explicit and clear
if name.startswith("A"):
    pass

if ".py" in filename:
    pass

# ❌ Incorrect — relies on indexing magic
if name[:1] == "A":
    pass

if filename[-3:] == ".py":
    pass
```

### Exception Handling
```python
# ✅ Correct — minimal try block, specific exceptions
try:
    value = int(user_input)
except ValueError:
    print("Invalid integer")

# ❌ Incorrect — too broad
try:
    value = int(user_input)
    process_data(value)
    save_to_db(value)
except:
    print("Error")
```

## Repository-Specific Rules

### For Learning Files (`*_demo.py` and `*_task.py`)

1. **Always follow PEP 8** — students learn from examples
2. **No overly complex code** — prioritize clarity over cleverness
3. **Include expected output** in comments for demo files
4. **Use meaningful variable names** — `user_age` not `ua`
5. **One concept per example** — don't mix multiple ideas
6. **Add docstrings to all functions** — even in learning files

### Example from This Repo

```python
# ✅ Good learning file structure
"""
Микро-задача: Variables and Types
"""

def celsius_to_fahrenheit(celsius):
    """Convert temperature from Celsius to Fahrenheit."""
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


print("=== Temperature Conversion ===")
temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")
# Expected output: 25°C = 77.0°F
```

## Summary Checklist

When writing or modifying code in this repository:

- [ ] 4 spaces for indentation (never tabs)
- [ ] Lines ≤ 79 characters
- [ ] Functions and variables: `snake_case`
- [ ] Classes: `PascalCase`
- [ ] Constants: `ALL_CAPS`
- [ ] Imports organized (stdlib → third-party → local)
- [ ] No spaces inside parentheses/brackets
- [ ] Single space around operators (`x = 1`, not `x=1`)
- [ ] Docstrings for all public functions/classes
- [ ] `isinstance()` for type checks, not `type()`
- [ ] `is None`, not `== None`
- [ ] Comments explain WHY, not WHAT

## Philosophy

> "A foolish consistency is the hobgoblin of little minds" — Emerson (quoted in PEP 8)

PEP 8 is a style guide, not law. **Readability within the context of this project takes priority.** However, for a learning repository, consistency and clarity are paramount—code is read far more than it is written.

---

**Last updated:** 2026-06-17  
**Version:** PEP 8 (latest from https://peps.python.org/pep-0008/)
