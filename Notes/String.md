# String

## Python

### Basics Notions
- Strings are immutable sequences of characters.
```python
s = "Hello World"
s[0] = "h"  # TypeError: 'str' object does not support item assignment

s = "hello world"  # This is allowed
# The original string is not modified, a new string is created. Then the original string is garbage collected.

# Notation, 
s = "Hello World"
print(id(s))  # Output: 4548923056
s1 = s
print(id(s1))  # Output: 4548923056
s = "Hello Universe" # a new string is created, and s is pointing to the new string
print(id(s))  # Output: 4545223288
print(id(s1))  # Output: 4548923056
```
- Strings can be enclosed in single quotes ('...') or double quotes ("...").
- Triple quotes ('''...''' or """...""") are used to span the string across multiple lines.
- Escape sequences are used to represent characters that are difficult to type or would be inconvenient to read.
```python
s = "Hello\nWorld"
print(s)  # Output: Hello
          #         World
```

### Basic Operations
- Length: Getting the length of a string using len(string).
```python
s = "Hello World"
print(len(s))  # Output: 11
```
- Concatenation: Combining strings using the + operator.
```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  # Output: Hello World
```
- Repetition: Repeating strings using the * operator.
```python
s = "Hello"
s1 = s * 3
print(s1)  # Output: HelloHelloHello
```
- Indexing: Accessing characters by index using string[index].
```python
s = "Hello"
print(s[0])  # Output: H
print(s[1])  # Output: e
```
- Slicing: Getting a substring using string[start:end:step].
```python
s = "Hello World"
print(s[0:5])  # Output: Hello
print(s[6:])  # Output: World
print(s[:5])  # Output: Hello
print(s[::2])  # Output: HloWrd
```
### String Methods
- .find(sub[, start[, end]]): Returns the lowest index where the substring sub is found.
```python
s = "Hello World"
print(s.find("World"))  # Output: 6

```
- .replace(old, new[, count]): Returns a string where all occurrences of 'old' are replaced by 'new'.
```python
s = "Hello World Hello World"
print(s.replace("World", "Universe"))  # Output: Hello Universe Hello Universe
```
- .split(sep=None, maxsplit=-1): Returns a list of the words in the string, using sep as the delimiter.
```python
s = "Hello World"
print(s.split())  # Output: ['Hello', 'World']
print(s.split("o"))  # Output: ['Hell', ' W', 'rld']
```
- .join(iterable): Joins an iterable of strings with the string acting as the separator.
```python
s = " "
print(s.join(["Hello", "World"])) # Output: Hello World
```
- .strip([chars]): Returns a copy of the string with leading and trailing characters removed.
```python
s = "  Hello World  "
print(s.strip())  # Output: Hello World, leading and trailing spaces removed
print(s.strip("  "))  # Output: Hello World, leading and trailing spaces removed
print(s.strip("  H"))  # Output: ello World, leading and trailing spaces and H removed
```
- .lstrip([chars]), .rstrip([chars]): Similar to .strip(), but for leading and trailing characters, respectively.
- .upper(), .lower(): Returns a copy of the string converted to uppercase or lowercase.
```python
s = "Hello World"
print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world
```
- .title(): Returns a title-cased version of the string.
```python
s = "hello world"
print(s.title())  # Output: Hello World
```
- .startswith(prefix[, start[, end]]), .endswith(suffix[, start[, end]]): Returns True if the string starts or ends with the specified prefix/suffix.
```python
s = "Hello World"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World"))  # Output: True
```
- .isdigit(), .isalpha(), .isalnum(), .isspace(): Return True if all characters in the string are digits, alphabetic, alphanumeric, or whitespace, respectively.
```python
s = "Hello World"
s1 = "123"
s2 = "HelloWorld123"
print(s.isdigit())  # Output: False
print(s.isalpha())  # Output: False
print(s.isalnum())  # Output: False
print(s.isspace())  # Output: False
print(s1.isdigit()) # Output: True
print(s1.isalpha()) # Output: False
print(s1.isalnum()) # Output: True
print(s1.isspace()) # Output: False
print(s2.isdigit()) # Output: False
print(s2.isalpha()) # Output: False
print(s2.isalnum()) # Output: True
print(s2.isspace()) # Output: False
```

### Formatting
- .format(*args, **kwargs): Formats the string using format specification.
```python
s = "Hello {}"
print(s.format("World"))  # Output: Hello World
print("Hello {0}, {1}".format("World", "Universe"))  # Output: Hello World, Universe
```
- f-strings (formatted string literals): Allows including expressions inside string literals, using {expression}.
```python
name = "World"
print(f"Hello {name}") # Output: Hello World
```
- .center(width[, fillchar]), .ljust(width[, fillchar]), .rjust(width[, fillchar]): Methods for aligning strings within a specified width.
```python
s = "Hello"
print(s.center(10, "-"))  # Output: --Hello---
### Searching and Matching
- .count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of substring sub in the string.
```python
s = "Hello World"
print(s.count("o")) # Output: 2
print(s.count("o", 0, 5)) # Output: 1
``` 

## String interning

String Interning: Python automatically interns certain strings. This means that for some strings, Python will store only one copy of the string in memory, even if it appears multiple times in a program. When you create a new variable that has the same string value as an interned string, Python will just point the new variable to the already-existing string object. This is why you might see the same id for different variables that are assigned the same string value.

Criteria for Interning: Python automatically interns string literals that look like identifiers, i.e., strings that could be variable names (containing letters, digits, and underscores, and not starting with a digit). This is because such strings are very likely to appear multiple times in programs (e.g., as variable names, attribute names, etc.), so interning them can save memory. However, not all strings are interned automatically. Python's rules for automatic interning can vary based on implementation details and the context in which the string is created.

Manual Interning: You can force strings to be interned using the sys.intern() function. This can be useful if you have determined through profiling that your program would benefit from interning strings that are not automatically interned by Python.

Implementation Details: Whether or not strings are interned can depend on how they are created and what they contain. For example, string literals in source code that are identical might be interned automatically by Python, but strings created at runtime through concatenation, user input, or other dynamic means might not be.

Python Version and Implementation: Different versions of Python and different Python implementations (e.g., CPython, PyPy) may handle interning differently, both in terms of which strings are interned and how interning is implemented.