class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> res;
        int n = candies.size();
        int maxCandies = 0;

        for(int i =0; i < n; i++ ){
            if(candies[i] > maxCandies){
                maxCandies = candies[i];
            }
        }

        for(int i = 0; i < n; i++){
            if(candies[i] + extraCandies >= maxCandies){
                res.push_back(true);
            } else{
                res.push_back(false);
            }
        }

        return res;
        

    }
};