# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


        
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        q = deque()
        q.append([root, 0])
        res = 0

        while(len(q) > 0):
            size = len(q)
            min_idx = 0
            max_idx = 0
            for i in range(size):
                [node, curr_idx] = q.popleft()

                if i == 0:
                    min_idx = curr_idx
                
                if i == size - 1:
                    max_idx = curr_idx

                if node.left:
                    q.append([node.left, 2*curr_idx+1])
                
                if node.right:
                    q.append([node.right, 2*curr_idx+2])
            
            res = max(res, max_idx - min_idx+1)

        return res 