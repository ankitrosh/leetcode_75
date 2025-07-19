class Solution {
public:
    int pivotIndex(vector<int>& nums) {
         int n = nums.size();
    if (n == 0) return -1;

    vector<int> prefixes(n);
    prefixes[0] = nums[0];
    for (int i = 1; i < n; ++i) {
        prefixes[i] = prefixes[i - 1] + nums[i];
    }

    vector<int> suffixes(n);
    suffixes[n - 1] = nums[n - 1];
    for (int i = n - 2; i >= 0; --i) {
        suffixes[i] = suffixes[i + 1] + nums[i];
    }

    for (int i = 0; i < n; ++i) {
        int leftSum  = (i > 0 ? prefixes[i - 1] : 0);
        int rightSum = (i + 1 < n ? suffixes[i + 1] : 0);
        if (leftSum == rightSum) {
            return i;
        }
    }

    return -1;
    }
};