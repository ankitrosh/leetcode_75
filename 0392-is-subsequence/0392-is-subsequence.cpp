class Solution {
public:
    bool isSubsequence(string s, string t) {

        if(s.size() == 0){
            return true;
        }
        if(t.size() < s.size()){
            return false;
        }
        int i = 0;

        for(int j=0; j<t.size(); j++){

            if(i == s.size()){
                return true;
            }

            if(s[i] == t[j]){    
                i++;
            }

        }

        if(i == s.size()){
                return true;
        }

        return false;
    }
};