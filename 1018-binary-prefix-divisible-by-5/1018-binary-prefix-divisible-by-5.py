class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:

        curr_sum = 0
        res = []

        for i in range(len(nums)):
            curr_sum = 2*(curr_sum) + nums[i]
            if curr_sum%5 == 0:
                res.append(True)
            else:
                res.append(False)
        
        return res
        