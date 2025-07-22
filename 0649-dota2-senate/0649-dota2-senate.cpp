class Solution {
public:
    string predictPartyVictory(string senate) {
        queue<int> d;
        queue<int> r;
        int n = senate.size();
        for(int i=0; i < n; i++){
            if(senate[i] == 'R'){
                r.push(i);
            } else {
                d.push(i);
            }
        }

        while(r.size() > 0 && d.size() > 0){
            int x1 = r.front();
            int x2 = d.front();

            if(x1 < x2){
                d.pop();
                r.pop();
                r.push(x1+n);
            } else {
                d.pop();
                r.pop();
                d.push(x2+n);
            }
        }

        if(r.empty()){
            return "Dire";
        }

        return "Radiant";
    }
};