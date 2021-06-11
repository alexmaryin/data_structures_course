# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val) + str(self.next) if self.next else str(self.val)


class Solution:
    def __init__(self):
        self.is_ten = False

    def addition(self, l1: ListNode, l2: ListNode) -> ListNode:
        add = (l1.val if l1 else 0) + (l2.val if l2 else 0)
        if self.is_ten:
            add += 1
        if add >= 10:
            self.is_ten = True
            add -= 10
        else:
            self.is_ten = False
        is_l1_next = l1.next if l1 and l1.next else None
        is_l2_next = l2.next if l2 and l2.next else None
        not_finish = is_l2_next or is_l1_next
        tail_var = ListNode(1) if self.is_ten else None
        return ListNode(add, self.addition(is_l1_next, is_l2_next) if not_finish else tail_var)


if __name__ == '__main__':
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    res = Solution().addition(l1, l2)
    print(res)
    assert str(res) == str(ListNode(7, ListNode(0, ListNode(8))))
