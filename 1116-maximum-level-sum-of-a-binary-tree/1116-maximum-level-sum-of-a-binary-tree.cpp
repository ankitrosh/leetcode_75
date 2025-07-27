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
    int maxLevelSum(TreeNode* root) {
        vector<int> rightView;
        
        if(!root){
            return 0;
        }
        queue<TreeNode*> q;
        int maxSum = root->val;
        int maxLevel = 1;
        int currLevel = 1;
        q.push(root);
        while(!q.empty()){
            int len = q.size();
            TreeNode*  node = NULL;
            int sum = 0;
            for(int i=0; i < len; i++){
                node = q.front();
                sum += node->val;
                q.pop();
                if(node->left){
                    q.push(node->left);

                }

                if(node->right){
                    q.push(node->right);
                }
            }
            if(maxSum < sum){
                maxSum = sum;
                maxLevel = currLevel;
            }
            currLevel++;
            
        }

        return maxLevel;
    }
};

