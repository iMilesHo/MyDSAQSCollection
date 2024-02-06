from typing import List
import unittest

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}

        for i in s:
            if dict_s.get(i) is None:
                dict_s[i] = 1
            else:
                dict_s[i] += 1

        for i in t:
            if dict_t.get(i) is None:
                dict_s[i] = 1
            else:
                dict_t[i] += 1

        for key in dict_s:
            if (dict_t[key] is None) or (dict_t[key] != dict_s[key]):
                return false
        return true

# Unit test for Solution class
class TestSolution(unittest.TestCase):
    def test_longestCommonPrefix(self):
        sol = Solution()

        # Test case 1: General case
        self.assertEqual(sol.longestCommonPrefix(["flower","flow","flight"]), "fl")

        # Test case 2: No common prefix
        self.assertEqual(sol.longestCommonPrefix(["dog","racecar","car"]), "")

        # Test case 3: All strings are the same
        self.assertEqual(sol.longestCommonPrefix(["test", "test", "test"]), "test")

        # Test case 4: List contains only one string
        self.assertEqual(sol.longestCommonPrefix(["only"]), "only")

# This allows running the tests from the command line
if __name__ == '__main__':
    unittest.main()