#include "Solution.h"
#include <gtest/gtest.h>
#include <vector>

TEST(SolutionTest, BasicTest) {
    Solution sol;
    std::vector<int> nums = {1,2,3,4,5,6,7};
    EXPECT_EQ(sol.search(nums, 3), 2);
    EXPECT_EQ(sol.search(nums, 1), 0);
    EXPECT_EQ(sol.search(nums, 7), 6);
    EXPECT_EQ(sol.search(nums, 8), -1);
}