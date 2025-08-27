class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        priority_queue<int, std::vector<int>, std::greater<int>> pq(nums.begin(), nums.begin() + k);
        int n = nums.size();
        for(int i=k; i<n; i++){
 
            if( nums[i] > pq.top()){
                
               pq.pop();
               pq.push(nums[i]);
            }
            
        }

        int res = pq.top();

        return res;

    }
};