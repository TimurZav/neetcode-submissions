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
        if not head:
            return None

        # шаг 1 — создаём новые узлы
        old_to_new = {}
        cur = head
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        # шаг 2 — расставляем next и random
        cur = head
        while cur:
            if cur.next:
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next

        return old_to_new[head]