class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_length = len(strs[0])
        
        for str in (strs):
            if len(str) < min_length:
                min_length = len(str)
        
        for i in range(min_length):
            char = strs[0][i]
            for j in strs:
                if j[i] != char:
                    return res
            res += char
        
        return res


        