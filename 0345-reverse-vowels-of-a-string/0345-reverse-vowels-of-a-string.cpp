class Solution {
public:
    bool isVowel(char c){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U' ){
            return true;
        }

        return false;
    }

    string reverseVowels(string s) {
       

        int n = s.size();
        vector<char> temp;
        for(int i =0; i < n; i++){
            if(isVowel(s[i])){
                temp.push_back(s[i]);
            }
        }

        int m = temp.size();
        int j = m -1;

        for(int i =0; i < n; i++){
            if(isVowel(s[i])){
                s[i] = temp[j];
                j--;
            }
        }
        return s;
    }
};