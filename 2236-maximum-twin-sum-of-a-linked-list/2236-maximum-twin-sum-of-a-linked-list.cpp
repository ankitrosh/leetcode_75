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
        // vector<int> twinSums;

        // ListNode* curr = head;
        // int n =0;
        // while(curr != NULL){
        //     twinSums.push_back(curr->val);
        //     curr = curr->next;
        //     n++;

        // }
        // int res = twinSums[0] + twinSums[n-1];
        // for(int i = 1; i < n/2; i++){
        //     res = max(res, twinSums[i] + twinSums[n-i-1]);
        // }
        // return res;

        // no extra space

        ListNode* slow = head;
        ListNode* fast = head;
        int res = 0;

        while(fast && fast->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        ListNode* nextNode = NULL;
        ListNode* prev = NULL;
        while(slow){
            nextNode = slow->next;
            slow->next = prev;
            prev = slow;
            slow = nextNode;
        }

        ListNode* curr = head;
        while(prev){
            res = max(res, curr->val + prev->val);
            prev = prev -> next;
            curr = curr->next;
        }

        return res;
    }
};