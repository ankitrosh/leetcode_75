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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> rightView;
        
        if(!root){
            return rightView;
        }
        queue<TreeNode*> q;

        q.push(root);
        while(!q.empty()){
            int len = q.size();
            TreeNode*  node = NULL;
            for(int i=0; i < len; i++){
                node = q.front();
                
                q.pop();
                if(node->left){
                    q.push(node->left);

                }

                if(node->right){
                    q.push(node->right);
                }
            }

            rightView.push_back(node->val);

            
        }

        return rightView;
    }
};