# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head or not head.next:
            return None
        s = 1
        ptr = head
        while ptr.next:
            s+=1
            ptr = ptr.next
        s = s//2 
        ptr = head
        while s>1:
            ptr = ptr.next
            s-=1
        ptr.next = ptr.next.next
        return head
        