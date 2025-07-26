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
    int dfs(TreeNode* root, int direction, int length){
        if(root == NULL){
            return 0;
        }
    
        int left = 0;
        int right = 0;

        if(direction == 0){
            left = dfs(root->left, 0 ,1); // restarting count
            right = dfs(root->right, 1 ,length + 1); // continuing the count
        }

        if(direction == 1){
            left = dfs(root->left, 0 ,length + 1);
            right = dfs(root->right, 1 ,1);
        }
       
        
        return max(max(left, right), length);
    }
    int longestZigZag(TreeNode* root) {
        if(root == NULL){
            return 0;
        }

        return max(
            dfs(root->left, 0, 1),
            dfs(root->right, 1, 1)
        );
    }
};