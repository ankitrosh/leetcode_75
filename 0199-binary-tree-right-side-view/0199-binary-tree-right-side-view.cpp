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
        deque<TreeNode*> q;

        q.push_front(root);
        while(!q.empty()){
            int len = q.size();
            TreeNode* rightNode = q.back();
            rightView.push_back(rightNode->val);
            for(int i=0; i < len; i++){
                TreeNode* node = q.front();
                
                q.pop_front();
                if(node->left){
                    q.push_back(node->left);

                }

                if(node->right){
                    q.push_back(node->right);
                }
            }

            
        }

        return rightView;
    }
};