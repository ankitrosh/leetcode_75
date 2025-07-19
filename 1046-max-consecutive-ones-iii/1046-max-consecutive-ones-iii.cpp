class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
    
        int i = 0;
        int zeroCount = 0;
        int maxLen = 0;
        int n = nums.size();
        
        for (int j = 0; j < n; ++j) {
            // Include nums[j] in the window
            if (nums[j] == 0) {
                ++zeroCount;
            }
            
            // If too many zeros, shrink from the left
            while (zeroCount > k) {
                if (nums[i] == 0) {
                    --zeroCount;
                }
                ++i;
            }
            
            // Now [i..j] has at most k zeros
            maxLen = max(maxLen, j - i + 1);
        }
        
        return maxLen;
    }
};