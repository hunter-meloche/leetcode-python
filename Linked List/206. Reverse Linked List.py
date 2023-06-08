# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        current_node = head
        previous_node = None
        next_node = None

        while current_node:
            next_node = current_node.next
            if not previous_node:
                current_node.next = None
            else:
                current_node.next = previous_node
            previous_node = current_node
            if next_node is not None:
                current_node = next_node
            else:
                break

        return current_node
