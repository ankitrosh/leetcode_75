/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    int pairSum(ListNode* head) {
        vector<int> twinSums;

        ListNode* curr = head;
        int n =0;
        while(curr != NULL){
            twinSums.push_back(curr->val);
            curr = curr->next;
            n++;

        }
        int res = twinSums[0] + twinSums[n-1];
        for(int i = 1; i < n/2; i++){
            res = max(res, twinSums[i] + twinSums[n-i-1]);
        }
        return res;
    }
};