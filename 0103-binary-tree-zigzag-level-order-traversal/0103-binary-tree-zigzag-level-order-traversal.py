# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        q = deque()

        res = []
        q.append(root)
        fromLeft = True
        while len(q) > 0:
            level = []
            size = len(q)
            print(fromLeft)
            for i in range(size):
                node = None
                
                node = q.popleft()
                
                level.append(node.val)
                # if(fromLeft == True):
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
                # else:
                #     if node.right != None:
                #         q.append(node.right)
                #     if node.left != None:
                #         q.append(node.left)
            
            if fromLeft == False:
                level.reverse()

            fromLeft =  not fromLeft
            
            res.append(level)
        
        return res

        
