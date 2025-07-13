class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int size = flowerbed.size();
        int availableSpots = 0;
        if(n == 0){
            return true;
        }
        if(size == 1){
            return !flowerbed[0];
        }
        for(int i = 0; i < size; i++){
            if( i == 0){
                if(flowerbed[i] == 0 && flowerbed[i+1] == 0){
                    availableSpots++;
                    i++;
                }
            } else if (i == size-1){
                if(flowerbed[i] == 0 && flowerbed[i-1] == 0){
                    availableSpots++;
                    i++;
                }
            } 
            else {
                if(flowerbed[i] == 0 && flowerbed[i-1] == 0 && flowerbed[i+1] == 0){
                    availableSpots++;
                    i++;
                }
            }
        }

        if(availableSpots >= n){
            return true;
        }

        return false;
    }
};