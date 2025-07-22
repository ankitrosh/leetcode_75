class RecentCounter {
public:
    vector<int> req;
    RecentCounter() {
        
    }
    
    int ping(int t) {
        req.push_back(t);
        
        int n = req.size();
        int count =0;
        for(int i = n-1; i>=0; i--){
            if(req[i] >= t- 3000){
                count++;
            }
        }
        return count;
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */