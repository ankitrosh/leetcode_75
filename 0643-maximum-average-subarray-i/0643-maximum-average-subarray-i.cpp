class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double res = 0.0;
        double temp = 0.0;
        int n = nums.size();
        
        for(int i = 0; i < k; i++){
            temp += nums[i];
        }
        res = temp;
        for(int i = k; i < n; i++){
            if(temp > res){
                res = temp;
            }
            temp -= nums[i-k];
            temp += nums[i];
        }

        if(temp > res){
                res = temp;
        }

        return res/k;
        
    }
};