# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # пустой узел-заглушка
        tail = dummy        # tail — указатель на последний узел результата

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1   # присоединили узел из list1
                list1 = list1.next  # list1 двигается вперёд
            else:
                tail.next = list2   # присоединили узел из list2
                list2 = list2.next  # list2 двигается вперёд
            tail = tail.next        # tail двигается на присоединённый узел

        tail.next = list1 if list1 else list2  # присоединяем остаток

        return dummy.next