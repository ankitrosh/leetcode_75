# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root == None:
            return []

        q = deque()
        v = 0
        level = 0
        q.append([root, v])
        nodes = {}
        vmin = float('inf')
        vmax = float('-inf')
        while len(q) > 0:
            size = len(q)
            
            for i in range(size):
                [node, nodev] = q.popleft()
                if nodev < vmin:
                    vmin = nodev
                if nodev > vmax:
                    vmax = nodev
                print(node.val, nodev)
                if node.left:
                    q.append([node.left, nodev-1])
                if node.right:
                    q.append([node.right, nodev+1])

                if nodev in nodes:

                    if level in nodes[nodev]:
                        nodes[nodev][level].append(node.val)
                        nodes[nodev][level].sort()
                    else:
                        nodes[nodev][level] = [node.val]
                else:
                    nodes[nodev] = {}
                    nodes[nodev][level] = [node.val]


            level += 1
        res = []
        print(nodes)
        for i in range(vmin, vmax+1):
            vlevels = nodes[i]
            res.append(list(vlevels.values()))
        res= [ [item for sublist in group for item in sublist] for group in res ]
        
        return res

        


            



            