# String

## Python

### Basic Operations
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

- Slicing: Getting a substring using string[start:end:step].
### String Methods
- .find(sub[, start[, end]]): Returns the lowest index where the substring sub is found.
- .replace(old, new[, count]): Returns a string where all occurrences of 'old' are replaced by 'new'.
- .split(sep=None, maxsplit=-1): Returns a list of the words in the string, using sep as the delimiter.
- .join(iterable): Joins an iterable of strings with the string acting as the separator.
- .strip([chars]): Returns a copy of the string with leading and trailing characters removed.
- .lstrip([chars]), .rstrip([chars]): Similar to .strip(), but for leading and trailing characters, respectively.
- .upper(), .lower(): Returns a copy of the string converted to uppercase or lowercase.
- .title(): Returns a title-cased version of the string.
- .startswith(prefix[, start[, end]]), .endswith(suffix[, start[, end]]): Returns True if the string starts or ends with the specified prefix/suffix.
- .isdigit(), .isalpha(), .isalnum(), .isspace(): Return True if all characters in the string are digits, alphabetic, alphanumeric, or whitespace, respectively.
Formatting
- .format(*args, **kwargs): Formats the string using format specification.
f-strings (formatted string literals): Allows including expressions inside string literals, using {expression}.
- .center(width[, fillchar]), .ljust(width[, fillchar]), .rjust(width[, fillchar]): Methods for aligning strings within a specified width.
### Searching and Matching
- .count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of substring sub in the string.