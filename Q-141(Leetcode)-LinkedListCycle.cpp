class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode*,int >m;
        ListNode *temp=head;
        while(temp){
            m[temp]++;
            if(m[temp]==2)
            {
                return true;
            }
            temp=temp->next;
        }
        return false;
    }
};
