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
