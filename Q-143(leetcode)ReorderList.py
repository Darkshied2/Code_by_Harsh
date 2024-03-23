if head==None or head.next==None or head.next.next==None:
            return head
        temp=head
        prev=None
        while temp.next!=None:
            prev=temp
            temp=temp.next
        prev.next=None
        ans= self.reorderList(head.next)
        head.next=temp
        temp.next=ans
        # ans.next=None
        return head
