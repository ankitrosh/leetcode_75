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
    ListNode* oddEvenList(ListNode* head) {
        // if(head == NULL || head->next == NULL){
        //     return head;
        // }
        // ListNode* curr = head;
        // ListNode* res = new ListNode(curr->val, NULL);
        // ListNode* temp = res;
        // while(curr != NULL && curr->next != NULL){
            
        //     curr = curr->next->next;
        //     if(curr){
        //         res->next = new ListNode(curr->val, NULL);
        //         res= res->next;
        //     }
            
        // }
        // curr = head->next;
        // res->next = new ListNode(curr->val, NULL);
        // res = res->next;
        // while(curr != NULL && curr->next != NULL){
        //     cout << curr->val << endl;
        //     curr = curr->next->next;
        //     if(curr){
        //         res->next = new ListNode(curr->val, NULL);
        //         res= res->next;
        //     }
        // }

        
        
        // return temp;

        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode* curr = head;
        ListNode* next = head->next;
        ListNode* temp = head->next;


        while(next != NULL && next->next != NULL){

            curr->next = next->next;
            curr = curr->next;

            next->next = next->next->next;
            
            

            next = next->next;
        }

        curr->next = temp;

        return head;

    }
};