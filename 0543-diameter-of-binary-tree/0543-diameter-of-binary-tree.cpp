/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = 0;
    int dfs(TreeNode* root){
                if(root == NULL){
            return 0;
        }

        int left = 0;
        int right = 0;


        if(root->left){
            left = dfs(root->left);
        }

        if(root->right){
            right = dfs(root->right);
        }
        res = max(left+right, res);

        return max(left, right) + 1;

    }
    int diameterOfBinaryTree(TreeNode* root) {
        
        dfs(root);
        return res;
    }
};