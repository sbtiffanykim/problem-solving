# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        # if the len(head) == 2
        if fast.next and (not fast.next.next):
            return slow.next

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            # To return the second middle node if there are two middle nodes
            if fast.next and (not fast.next.next):
                return slow.next
        return slow