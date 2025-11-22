class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        
        numOps = 0

        for num in nums:
            if num%3 != 0:
                temp = num%3
                if temp == 2:
                    numOps += 1
                else:
                    numOps += temp
            
        
        return numOps

