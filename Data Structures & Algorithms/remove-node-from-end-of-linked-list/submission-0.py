# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        slow = dummy
        fast = dummy

        # Сдвигаем fast вперёд на n+1 шагов — теперь между slow и fast разрыв в n узлов
        for _ in range(n + 1):
            fast = fast.next

        # Двигаем оба указателя, пока fast не дойдёт до конца (None)
        # slow окажется ровно перед узлом, который нужно удалить
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next