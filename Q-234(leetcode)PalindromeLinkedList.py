# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        fst,slw=head,head
        stk=[]
        while fst and fst.next is not None:
            stk.append(slw.val)
            slw= slw.next
            fst= fst.next.next
        if fst is not None:
            slw=slw.next
        while(slw and len(stk)) is not None:
            if stk.pop() !=slw.val:
                return False
            slw=slw.next
        return True
