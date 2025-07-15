class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        long long allProduct = nums[0];

        int n = nums.size();
        vector<int> prefix(n);
        vector<int> suffix(n);
        vector<int> res(n);
        res[0] = 1;
        
        for(int i=1; i<n; i++){
            res[i] = res[i-1]*nums[i-1];
        }
        
        int temp = nums[n-1];
        int temp2;
        nums[n-1] = 1;
        for(int i = n-1; i > 0; i--){
            temp2 = nums[i-1];
            nums[i-1] = nums[i]*temp;
            temp = temp2;
            
        }
        for(int i = 0; i < n; i++){

            res[i] = nums[i]*res[i];
        }

        return res;
        
    }
};