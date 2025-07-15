class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long long allProduct = nums[0];

        int n = nums.size();
        vector<int> prefix(n);
        vector<int> suffix(n);
        vector<int> res(n);
        prefix[0] = 1;
        
        for(int i=1; i<n; i++){
            prefix[i] = prefix[i-1]*nums[i-1];
        }
        suffix[n-1] = 1;
        for(int i = n-1; i > 0; i--){
            suffix[i-1] = suffix[i]*nums[i];
        }

        for(int i = 0; i < n; i++){
            res[i] = suffix[i]*prefix[i];
        }

        return res;
        
    }
};