class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int n = nums.size();
        int num_ops = 0;
        unordered_map<int, int> umap;
        umap.reserve(nums.size());                 // 1) allocate all buckets up‑front
        umap.max_load_factor(0.7f); 
        for(int i =0; i< n;i++){
            auto it = umap.find(k - nums[i]);
            if(it != umap.end()){
                num_ops++;
                // it->second -= 1;
                if(--it->second == 0){
                    umap.erase(it);
                }
            }  else {
               umap[nums[i]]++;
            }
        }

        return num_ops;

    }
};