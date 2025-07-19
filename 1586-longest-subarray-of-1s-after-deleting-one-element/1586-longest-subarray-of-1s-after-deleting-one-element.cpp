class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int n = nums.size();
    int j = 0, k = 1;                   // j = window start, k = flips remaining
    int prevZero = -1, lastZero = -1;   // track the last two zero positions
    int maxLen = 0;

    for (int i = 0; i < n; ++i) {
        if (nums[i] == 0) {
            k--;
            prevZero = lastZero;  // push the old lastZero into prevZero
            lastZero = i;         // update lastZero to the current zero
        }

        if (k < 0) {
            // we've used up our one allowed flip,
            // so slide j to just after the *previous* zero
            j = prevZero + 1;
            k++;
        }

        // i-j is the length of the window minus the one zero we'll delete
        maxLen = max(maxLen, i - j);
    }

    return maxLen;
    }
};