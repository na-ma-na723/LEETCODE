# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        s = 1
        ptr = head
        while ptr.next:
            s+=1
            ptr = ptr.next
        s = s//2 
        while s>0:
            head = head.next
            s-=1
        return head
