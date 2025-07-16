class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size();
        vector<int> res;
        int countZeros = 0;

        for(int i =0; i < n; i++){
            if(nums[i] != 0){
                res.push_back(nums[i]);
            } else {
                countZeros++;
            }
        }
        int m = res.size();
        for(int i = 0; i< m; i++){
            nums[i] = res[i];
        }

        for(int i=m; i<n; i++){
            nums[i] = 0;
        }
        
    }
};