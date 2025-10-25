# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root,res):

        if root.left != None:
            self.dfs(root.left,res)
        res.append(root.val)
        if root.right != None:
            self.dfs(root.right, res)


    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        

        if root == None:
            return []
        res = []

        
        self.dfs(root, res)
        
        return res
