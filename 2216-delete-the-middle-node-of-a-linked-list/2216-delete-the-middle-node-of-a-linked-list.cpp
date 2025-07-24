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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = head;
        while(fast != NULL && fast->next != NULL){
            fast = fast->next->next;
            prev = slow;
            slow = slow->next;
        }

        if(prev->next != NULL){
            prev->next = prev->next->next;
        } else {
            return NULL;
        }



        return head;
    }
};