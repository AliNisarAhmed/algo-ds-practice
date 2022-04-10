package arrays;

class Solution {
    public int dominantIndex(int[] nums) {
        int maxIndex = 0;
        int max = nums[0];

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > max) {
                max = nums[i];
                maxIndex = i;
            }
        }

       for (int x : nums) {
           if (x != max && max < 2 * x) {
               return -1;
           }
       }

       return maxIndex;
    }
}
