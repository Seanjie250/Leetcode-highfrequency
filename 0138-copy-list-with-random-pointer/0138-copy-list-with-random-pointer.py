"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = {None : None}
        cur = head
        while cur:
            temp[cur] = Node(cur.val)
            cur = cur.next
        
        print(temp)

        cur = head
        while cur:
            new_node = temp[cur]
            new_node.next = temp[cur.next]
            new_node.random = temp[cur.random]
            cur = cur.next
        return temp[head]


        