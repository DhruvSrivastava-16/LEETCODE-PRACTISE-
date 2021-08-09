class Solution {
    public int[] runningSum(int[] nums) {
        int cum_sum = 0;
        for(int i=0;i<nums.length;i++)
        {
            cum_sum = cum_sum + nums[i];
            nums[i] = cum_sum;
        }
        
        return nums;
        
    }
}