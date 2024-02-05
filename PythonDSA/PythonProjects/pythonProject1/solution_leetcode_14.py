from typing import List
import unittest

class Solution:
    def longestCommonPrefixBetween(self, str1: str, str2: str) -> str:
        ans = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                ans += str1[i]
            else:
                return ans
        return ans

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        temp = strs[0]
        for i in range(1, len(strs)):
            temp = self.longestCommonPrefixBetween(temp, strs[i])
        return temp

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