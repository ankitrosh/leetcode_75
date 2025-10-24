# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root == None:
            return 0;

        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right)+1)

        # q = deque();

        # q.append([root, 1]);
        # res = 0;
        # while q:
        #     node, level = q.popleft();
        #     res = max(res, level);
        #     if node.left:
        #         q.append([node.left, level+1]);
        #     if node.right:
        #         q.append([node.right,level+1]);

        # return res;
        
        