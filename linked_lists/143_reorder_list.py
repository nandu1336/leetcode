from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    # 1. find the mid point using slow and fast pointers
    # 2. split the second half into a separate list
    # 3. reverse the second linked list
    # 4. merge both halhfs

    # first part
    dummy = ListNode(0, head)
    slow, fast = dummy, dummy

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # second part
    second_half = slow.next
    slow.next = None

    # third part
    prev, cur = None, second_half

    while cur:
        nxt, cur.next = cur.next, prev
        prev, cur = cur, nxt

    # fourth part
    first, second = dummy.next, prev

    while second:
        temp1, temp2 = first.next, second.next
        first.next = second
        second.next = temp1
        first, second = temp1, temp2

    return head



if __name__ == "__main__":
    # head = [1, 2, 3, 4, 5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    res = reorder_list(head)
    values = []
    while res:
        values.append(res.val)
        res = res.next

    print(values)