# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = 1
        ptr = head
        while s<=n:
            s+=1
            ptr = ptr.next
        if ptr == None:
            return head.next
        ptr2 = head
        while ptr.next:
            ptr = ptr.next
            ptr2 = ptr2.next
        ptr2.next = ptr2.next.next
        return head