class Solution {
public:
    int compress(vector<char>& chars) {
        
        int i = 0;
        int n = chars.size();
        vector<char> res;
        for(int i=0; i < chars.size(); i++){
            int count = 1;
            char c = chars[i];
            while(i+1 < chars.size() && chars[i+1] == chars[i]){
                // chars.erase(chars.begin() + i);
                count++;
                i++;
            }

            res.push_back(c);
            
            if(count > 1){
                vector<char> temp;
                while(count > 0){
                    int rem = count%10;
                    temp.push_back(rem + '0');
                    count = count/10;
                }

                for(int j = temp.size()-1; j >=0; j--){
                    res.push_back(temp[j]);
                }
                
            }
        }

        int m = res.size();
        for(int j=0; j<m;j++){
            chars[j] = res[j];
        }

        return m;
    }
    
};