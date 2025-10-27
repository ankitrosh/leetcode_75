# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if root == None:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        if left and not right:
            return left
        
        if right and not left:
            return right


        # queue = deque();

        # queue.append(root);

        # parent ={root:None};

        # while queue:
        #     node = queue.popleft();

        #     if node.left:
        #         queue.append(node.left);
        #         parent[node.left] = node;
            
        #     if node.right:
        #         queue.append(node.right);
        #         parent[node.right] = node;
            
        #     if p in parent and q in parent:
        #         break;
        
        # ancestors = set();

        # while p:
        #     ancestors.add(p);
        #     p = parent[p];

        # while q:
        #     if q in ancestors:
        #         return q;
        #     q = parent[q];

        # return None; 





        