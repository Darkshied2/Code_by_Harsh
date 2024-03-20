# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        lst1,lst2= [],[]
        while list1:
            lst1.append(list1.val)
            list1 = list1.next
        while list2:
            lst2.append(list2.val)
            list2 = list2.next
        lst1[a:b+1]=lst2[:]
        a = ListNode(0)
        temp = a
        for i in lst1:
            temp.next = ListNode(i)
            temp = temp.next
        return a.next
