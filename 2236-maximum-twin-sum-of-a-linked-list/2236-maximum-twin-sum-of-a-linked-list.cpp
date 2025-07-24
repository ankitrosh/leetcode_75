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
        int n = 0;
        while(curr != NULL){
            twinSums.push_back(curr->val);
            n++;
            curr = curr->next;
        }

        // reverse the LL

        curr = head;
        ListNode* prev = NULL;
        ListNode* temp = NULL;

        while(curr != NULL){

            temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;

        }
        int i = 0;
        while(prev != NULL){
            twinSums[i] += prev->val;
            prev = prev->next;
            i++;
        }
        int res = twinSums[0];
        for(int j = 1; j < n; j++){
            res = max(res, twinSums[j]);
        }
        return res;
    }
};