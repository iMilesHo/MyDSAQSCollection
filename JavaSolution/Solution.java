package JavaSolution;

import java.util.ArrayList;
import java.util.List;

public class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        
        // Check each element in nums1 for uniqueness against nums2
        for (int num1 : nums1) {
            if (!contains(nums2, num1) && !list1.contains(num1)) {
                list1.add(num1);
            }
        }
        
        // Check each element in nums2 for uniqueness against nums1
        for (int num2 : nums2) {
            if (!contains(nums1, num2) && !list2.contains(num2)) {
                list2.add(num2);
            }
        }
        
        List<List<Integer>> result = new ArrayList<>();
        result.add(list1);
        result.add(list2);
        return result;
    }
    
    // Helper method to check if an array contains a specific element
    private boolean contains(int[] array, int key) {
        for (int element : array) {
            if (element == key) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {4, 9, 5};
        int[] nums2 = {9, 4, 9, 8, 4};
        List<List<Integer>> result = solution.findDifference(nums1, nums2);
        System.out.println(result);
        
    }
}
