## 448. Find All Numbers Disappeared in an Array

### Problem Statement

Check the problem statement [here](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/).

### My Solution

1. Manual Hash Table
   Time complexity: O(n)
   Space complexity: O(n)

```java
// Java
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // to skip the first index, since the range of elements is[1,n]
        int[] myHashTable = new int[nums.length+1];

        // initial myHashTable
        for(int i=1; i<=nums.length; i++){
            myHashTable[i] = 0;
        }

        for(int i=1; i<=nums.length; i++) {
            myHashTable[nums[i-1]] = 1;
        }

        List<Integer> ans = new ArrayList();;

        for(int i=1; i<=nums.length; i++){
            if(myHashTable[i]!=1){
                ans.add(i);
            }
        }

        return ans;
    }
}
```

2. A more efficient solution using the same concept
   Time complexity: O(n)
   Space complexity: O(1) (excluding the space for the answer)

```java
public class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> missingNumbers = new ArrayList<>();

        // Mark the positions corresponding to the numbers as negative
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1; // Adjust for 0-based indexing
            if (nums[index] > 0) {
                nums[index] = -nums[index]; // Mark as visited
            }
        }

        // Find positions not marked (these are the missing numbers)
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missingNumbers.add(i + 1); // Adjust for 1-based numbering
            }
        }

        return missingNumbers;
    }
}
```

## C++ version

```cpp
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        int n = nums.size();
        vector<int> ans;
        for (int i=0; i < n; i++) {
            int itr = abs(nums[i]) - 1;
            if (nums[itr] > 0) {
                nums[itr] = -nums[itr];
            }
        }

        for (int i=0; i < n; i++) {
            if (nums[i] > 0){
                ans.push_back(i+1);
            }
        }
        return ans;
    }
};
```

- use set to store the numbers

```cpp
#include <iostream>
#include <vector>
#include <set>

std::vector<int> findDisappearedNumbers(std::vector<int>& nums) {
    int n = nums.size();
    std::set<int> numSet;

    // Populate the set with all numbers from 1 to n
    for (int i = 1; i <= n; ++i) {
        numSet.insert(i);
    }

    // Remove numbers that are present in the array
    for (int num : nums) {
        numSet.erase(num);
    }

    // Convert the set to a vector
    return std::vector<int>(numSet.begin(), numSet.end());
}

int main() {
    std::vector<int> nums1 = {4, 3, 2, 7, 8, 2, 3, 1};
    std::vector<int> result = findDisappearedNumbers(nums1);

    std::cout << "Output: [";
    for (size_t i = 0; i < result.size(); ++i) {
        std::cout << result[i] << (i < result.size() - 1 ? ", " : "");
    }
    std::cout << "]" << std::endl;

    return 0;
}

```
