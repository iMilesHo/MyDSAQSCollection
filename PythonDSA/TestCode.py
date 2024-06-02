from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

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