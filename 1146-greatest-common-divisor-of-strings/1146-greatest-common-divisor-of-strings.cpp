class Solution {
public:
    int gcd(int x, int y){
        if( x == 0){
            return y;
        }

        if(y == 0){
            return x;
        }

        if(x > y){
            return gcd(x%y, y);
        }

        return gcd(y%x, x);
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