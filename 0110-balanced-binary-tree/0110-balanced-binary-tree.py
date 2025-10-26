# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def checkBalanced(self, root):

        if root == None:
            return [True, 0]
        
        if root.left == None and root.right == None:
            return [True, 1]

        [lbool, lheight] = self.checkBalanced(root.left)
        [rbool, rheight] = self.checkBalanced(root.right)
        if(abs(lheight - rheight) <= 1 and lbool and rbool):
            return (True, max(lheight, rheight) + 1)
        
        return [False, max(lheight, rheight)]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        [res, height] = self.checkBalanced(root)

        return res


        