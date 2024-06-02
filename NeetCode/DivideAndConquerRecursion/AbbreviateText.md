# Abbreviate Text

## Description

Given a text and a dictionary of abbreviations, abbreviate the text using the dictionary. The abbreviation should be done in such a way that the text is abbreviated as much as possible. If there are multiple ways to abbreviate the text, choose the one that results in the shortest abbreviation. If there are multiple ways to abbreviate the text with the same length, choose the one that results in the smallest index in the text.

## Example

1. "that" -> "th@"
2. if two words overlap, replace the first one, e.g. "atow" -> "@ow"
3. if there is two key, begin at the same index in the text we should replace the longer one right?
4. just return lowercase is fine

## Solution

```python
def abbreviate_text(text: str, abbrev_dict: dict) -> str:
    s = text.lower() # at times
    s_l = s.split(" ")
    def helper(s: str) -> str:
        if not s:
            return s
        if s in abbrev_dict:
            return abbrev_dict[s]

        # Find the available abbreviation
        available = {}
        for key in abbrev_dict:
            find_idx = s.find(key)
            if find_idx != -1:
                available[key] = find_idx
        if not available:
            return s

        # Find the longest abbreviation with the smallest index
        maxL = ""
        L_idx = -1
        for key in available:
            if len(key) > len(maxL) or (len(key) == len(maxL) and available[key] < L_idx):
                maxL = key
                L_idx = available[key]
        # Recursively abbreviate the string
        return helper(s[:L_idx]) + abbrev_dict[maxL] + helper(s[L_idx+len(maxL):])
    for idx in range(len(s_l)):
        s_l[idx] = helper(s_l[idx])
    return " ".join(s_l)

# Abbreviation dictionary
abbreviation_dict = {
    'at': '@',
    'and': '&',
    'you': 'u',
    'one': '1',
    'won': '1',
    'two': '2',
    'to': '2',
    'too': '2',
    'for': '4',
    'four': '4',
    'be': 'b',
    'bee': 'b',
    'are': 'r',
    'see': 'c',
    'sea': 'c',
    'oh': 'o',
    'why': 'y'
}

# Example usage
text_example = "That took me to four and been won atoh atwo ato"
print(text_example)
abbreviated_text = abbreviate_text(text_example, abbreviation_dict)
print(abbreviated_text)
```
