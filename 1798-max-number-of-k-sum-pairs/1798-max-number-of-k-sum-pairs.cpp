class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int n = nums.size();
        int num_ops = 0;
        unordered_map<int, int> umap;
        for(int i =0; i< n;i++){
            if(umap.find(k - nums[i]) != umap.end()){
                num_ops++;
                umap[k - nums[i]]--;
                if(umap[k-nums[i]] == 0){
                    umap.erase(k-nums[i]);
                }
            }  else {
               umap[nums[i]]++;
            }
        }

        return num_ops;

    }
};