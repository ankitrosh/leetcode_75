# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxSum(self, root):
        if root == None:
            return float('-inf')
        
        lsum = self.maxSum(root.left)
        rsum = self.maxSum(root.right)
        csum = root.val
        lval = root.val
        rval = root.val
        if lsum > 0:
            csum += lsum
            lval += lsum
        if rsum > 0:
            csum += rsum
            rval += rsum
        self.res = max(self.res, csum)
        print(root.val, csum, lsum, rsum, max(lval, rval)  )
        
        # 1 4 3 -3 4
        return max(lval, rval) 
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        self.maxSum(root)
        return self.res
        