class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        // vector<int>res;
        priority_queue<int,vector<int>,greater<int>>res;
        ListNode* new1=new ListNode(0);
        ListNode * temp1=new1;
        for(int i = 0;i< lists.size();i ++)
        {
            ListNode* temp = lists[i];
            while(temp != NULL)
            {
                cout<<temp->val<<" ";
                res.push(temp->val);
                temp = temp->next;
            }   
        }
        while(!res.empty()){
            ListNode * kl = new ListNode(res.top());
            temp1->next = kl;
            temp1=temp1->next;
            res.pop();
        }
    return new1->next;
        
    }
};

