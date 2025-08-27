class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        
        priority_queue<int, std::vector<int>, std::greater<int>> pq;
        int n = nums.size();
        for(int i=0; i<n; i++){
 
            if(pq.size() == k && nums[i] > pq.top()){
                cout << nums[i] << endl;
                
               pq.pop();
               pq.push(nums[i]);
            } else if(pq.size() < k){
              pq.push(nums[i]);

            }
            
        }

        int res = pq.top();

        return res;

    }
};