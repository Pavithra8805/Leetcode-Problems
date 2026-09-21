import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        if (nums == null || nums.length < 4) return result;

        Arrays.sort(nums);  
        int n = nums.length;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) continue;  

            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1]) continue; 

                int left = j + 1;
                int right = n - 1;

                while (left < right) {
                    long sum = (long) nums[i] + nums[j] + nums[left] + nums[right];

                    if (sum == target) {
                        result.add(Arrays.asList(nums[i], nums[j], nums[left], nums[right]));

                        while (left < right && nums[left] == nums[left + 1]) left++;
                        
                        while (left < right && nums[right] == nums[right - 1]) right--;

                        left++;
                        right--;
                    } else if (sum < target) {
                        left++;
                    } else {
                        right--;
                    }
                }
            }
        }

        return result;
    }

    // Method for Product of Array Except Self Problem
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];

        // Step 1: Initialize answer array with prefix products
        answer[0] = 1; // There are no elements to the left of the first element
        for (int i = 1; i < n; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
        }

        // Step 2: Traverse from the end to build suffix product and multiply
        int suffixProduct = 1; // No elements to the right of the last element
        for (int i = n - 1; i >= 0; i--) {
            answer[i] = answer[i] * suffixProduct;
            suffixProduct *= nums[i];
        }

        return answer;
    }

    public static void main(String[] args) {
        // Test for fourSum
        Solution solver = new Solution();
        int[] numsForFourSum = {1, 0, -1, 0, -2, 2};
        int target = 0;
        List<List<Integer>> resultForFourSum = solver.fourSum(numsForFourSum, target);
        System.out.println("4-SUM Result: " + resultForFourSum);

        // Test for productExceptSelf
        int[] numsForProduct = {1, 2, 3, 4};
        int[] resultForProduct = solver.productExceptSelf(numsForProduct);
        System.out.print("Product Except Self Result: ");
        for (int num : resultForProduct) {
            System.out.print(num + " ");
        }
    }
}