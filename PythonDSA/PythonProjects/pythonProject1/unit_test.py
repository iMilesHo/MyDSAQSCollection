import unittest

# Unit test for Solution class
# class TestSolution(unittest.TestCase):
#     def test_longestCommonPrefix(self):
#         sol = Solution()
#
#         # Test case 1: General case
#         self.assertEqual(sol.longestCommonPrefix(["flower","flow","flight"]), "fl")
#
#         # Test case 2: No common prefix
#         self.assertEqual(sol.longestCommonPrefix(["dog","racecar","car"]), "")
#
#         # Test case 3: All strings are the same
#         self.assertEqual(sol.longestCommonPrefix(["test", "test", "test"]), "test")
#
#         # Test case 4: List contains only one string
#         self.assertEqual(sol.longestCommonPrefix(["only"]), "only")
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
