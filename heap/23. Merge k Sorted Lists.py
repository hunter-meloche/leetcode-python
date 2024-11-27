# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return

        heap = []
        head = tail = ListNode(0) # head and tail reference same dummy object initially

        # Puts the heads of each ListNode object in lists into the heap
        for i,listnode in enumerate(lists):
            if listnode:
                heapq.heappush(heap, (listnode.val, i, listnode))
        
        while heap:
            node = heapq.heappop(heap)[2] # Removes the ListNode object with the lowest value from the heap
            tail.next = node # Assigns the new node to the next value of the tail
            tail = tail.next # We abandon our reference to the previous object and point tail to the latest object in the list
            if node.next: # If the current node has a next value, it should be added to the heap
                i += 1
                heapq.heappush(heap, (node.next.val, i, node.next))

        return head.next # head has a dummy value so we pass the next object
