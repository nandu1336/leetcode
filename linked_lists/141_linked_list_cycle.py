from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False 

if __name__ == "__main__":
    three = ListNode(3)
    two = ListNode(2)
    zero = ListNode(0)
    four = ListNode(4)

    three.next = two
    two.next = zero
    zero.next = four
    four.next = two

    print(has_cycle(three))
        