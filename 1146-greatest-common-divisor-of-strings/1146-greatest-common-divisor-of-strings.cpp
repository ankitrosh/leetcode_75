class Solution {
public:
    int gcd(int x, int y){
        while(y != 0){
            int temp = x%y;
            x = y;
            y = temp;
        }

        return x;
    }
    string gcdOfStrings(string str1, string str2) {
        


        if( str1 + str2 != str2 + str1){
            return "";
        }
  
        int n = str1.size();
        int m = str2.size();
        string res = "";

        int x = gcd(n, m);
        return str1.substr(0, x);
    }
};