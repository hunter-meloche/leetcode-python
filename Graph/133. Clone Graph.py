"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Handles empty node inputs
        if not node:
            return node
            
        # Creates a deque, which allows for bidirectional insertions and pops
        q = deque([node])
        # Creates a dictionary that tracks the creation of cloned nodes
        clones = {node.val: Node(node.val, [])}

        # Iterates through each node and its neighbors
        while q:
            # Removes current node from deque
            curr = q.popleft()
            # Finds current clone in dict
            curr_clone = clones[curr.val]

            # Iterates through node's neighbors
            for neighbor in curr.neighbors:
                # Inserts neighbor into clone dict and deque so its own neighbors can be examined
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)

                # Neighbors are inserted into current clone
                curr_clone.neighbors.append(clones[neighbor.val])

        return clones[node.val]
