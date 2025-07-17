class Solution {
public:
    bool isVowel(char c){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
            return true;
        }

        return false;
    }

    int maxVowels(string s, int k) {
        int n = s.size();

        int res = 0;
        int temp = 0;
        for(int i =0; i < k; i++){
            if(isVowel(s[i])){
                temp++;
            }
        }

        for(int i=k; i<n;i++){
            if(temp > res){
                res = temp;
            }

            if(isVowel(s[i-k])){
                temp--;
            }

            if(isVowel(s[i])){
                temp++;
            }
        }

        if(temp > res){
                res = temp;
        }

        return res;
        
    }
};