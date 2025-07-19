class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int res = 0;
        int n = gain.size();
        int curr_height = 0;

        for(int i = 0; i < n; i++){
            curr_height += gain[i];

            res = max(res, curr_height);
        }

        return res;
        
    }
};