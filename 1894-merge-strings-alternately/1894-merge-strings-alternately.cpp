class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string res = "";
        int n = word1.size();
        int m = word2.size();
        bool flag = true;
        int i = 0;
        int j = 0;
        while( i < n && j < m){
            if(flag){
                res += word1[i];
                i++;
                flag = !flag;
            } else {
                res += word2[j];
                j++;
                flag = !flag;
            }
        }

        while(i < n){
            res += word1[i];
            i++;
        }

        while(j < m){
            res += word2[j];
            j++;
        }

        return res;
    }
};