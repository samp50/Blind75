class Solution {    
    public int findMiddleIndex(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum = sum + nums[i];
        }
        int prefixSum = 0;
        for (int j = nums.length; j > 0; j--) {
            prefixSum = prefixSum + nums[j - 1];
            if (prefixSum == (sum - prefixSum - j)) {
                return j;
            }
        }
        return -1;
    }
}