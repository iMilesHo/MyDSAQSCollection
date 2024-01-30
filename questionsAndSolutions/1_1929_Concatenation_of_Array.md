## [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/description/)

### Problem Statement
Check the problem statement [here](https://leetcode.com/problems/concatenation-of-array/description/).

### My Solution

```java
// Java
class Solution {
    public int[] getConcatenation(int[] nums) {
        int length = nums.length;
        int[] ans = new int[2*length];
        for(int i=0; i < length; i++){
            ans[i] = nums[i];
            ans[i+length] = nums[i];
        }
        return ans;
    }
}
```

