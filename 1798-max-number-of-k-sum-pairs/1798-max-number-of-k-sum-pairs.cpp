class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int num_ops = 0;
        unordered_map<int, int> umap;
        for(int i =0; i< n;i++){
            if(umap.find(k - nums[i]) != umap.end()){
                num_ops++;
                umap[k - nums[i]] -= 1;
                if(umap[k-nums[i]] == 0){
                    umap.erase(k-nums[i]);
                }
            } else if(umap.find(nums[i]) != umap.end()){
                umap[nums[i]] += 1;
            } else {
                umap.emplace(nums[i], 1);
            }
        }
       

        return num_ops;


    }
};