class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> st;  // use as stack
        for (int a : asteroids) {
            bool destroyed = false;
            // only possible collision: incoming a is moving left (a<0) and stack top > 0
            while (!st.empty() && a < 0 && st.back() > 0) {
                if (abs(st.back()) < abs(a)) {
                    // top is smaller: it explodes
                    st.pop_back();
                    continue;           // keep checking against new top
                }
                else if (abs(st.back()) == abs(a)) {
                    // both explode
                    st.pop_back();
                }
                // either way (equal or top bigger) our asteroid a is destroyed
                destroyed = true;
                break;
            }
            if (!destroyed) {
                st.push_back(a);
            }
        }
        return st;
        

        
    }
};