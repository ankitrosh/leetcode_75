class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
    
        int left = 0;
        int zeroCount = 0;
        int maxLen = 0;
        int n = nums.size();
        
        for (int right = 0; right < n; ++right) {
            // Include nums[right] in the window
            if (nums[right] == 0) {
                ++zeroCount;
            }
            
            // If too many zeros, shrink from the left
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    --zeroCount;
                }
                ++left;
            }
            
            // Now [left..right] has at most k zeros
            maxLen = max(maxLen, right - left + 1);
        }
        
        return maxLen;
    }
};