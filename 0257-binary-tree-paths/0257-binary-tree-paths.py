# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        if root == None:
            return []
        
        res = []

        def buildPaths(node, path):
            if not node:
                return
            
            new_path = path + str(node.val)

            if not node.left and not node.right:
                res.append(new_path)
            
            new_path  += '->'

            buildPaths(node.left, new_path)
            buildPaths(node.right, new_path)
        
        buildPaths(root, "")

        return res

        
        
        
        