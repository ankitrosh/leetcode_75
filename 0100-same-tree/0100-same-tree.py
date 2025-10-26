# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:


        # q1 = deque();
        # q2 = deque();

        # if not p and not q:
        #     return True;
        # if (not p and q) or (p and not q):
        #     return False;
        # q1.append(p);
        # q2.append(q);

        # while q1 and q2:
            
        #     lenq1 = len(q1);
        #     lenq2 = len(q2);
        #     if lenq1 != lenq2:
        #         return False;
        #     for i in range(lenq1):
        #         node1 = q1.popleft();
        #         node2 = q2.popleft();

        #         if node1.val != node2.val:
        #             return False;
        #         if node1.left and node2.left:
        #             if node1.left.val != node2.left.val:
        #                 return False;
        #             else:
        #                 q1.append(node1.left);
        #                 q2.append(node2.left);
        #         elif (node1.left and not node2.left) or (not node1.left and node2.left):
        #             return False;
                
        #         if node1.right and node2.right:
        #             if node1.right.val != node2.right.val:
        #                 return False;
        #             else:
        #                 q1.append(node1.right);
        #                 q2.append(node2.right);
        #         elif (node1.right and not node2.right) or (not node1.right and node2.right):
        #             return False;
        # if len(q1) != len(q2):
        #     return False;
        # return True;

        if p == None and q == None:
            return True
        
        if p == None or q == None:
            return False
        

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)


