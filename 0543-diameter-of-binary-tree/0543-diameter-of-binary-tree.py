# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getDiameter(self,root): 

        if root == None:
            return [0,0]
        
        [lDiameter, lheight] = self.getDiameter(root.left)

        [rDiameter, rheight] = self.getDiameter(root.right)

        diameter = lheight + rheight

        return [max(diameter, lDiameter, rDiameter), max(lheight, rheight) + 1] 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        [res, height] = self.getDiameter(root)
        return res

                





        