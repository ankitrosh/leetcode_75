class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int i = 0;
        int j = n-1;
        int num_ops = 0;
        while(j > i){
            if(nums[i] + nums[j] == k){
                num_ops++;
                i++;
                j--;
            } else if(nums[i] + nums[j] < k){
                i++;
            } else {
                j--;
            }
        }

        return num_ops;


    }
};