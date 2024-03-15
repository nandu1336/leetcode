from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return 
    
    dummy = ListNode()
    tail = dummy

    while list1 and list2:
        if list1.val > list2.val:
            tail.next = list2
            list2 = list2.next
        else:
            tail.next = list1
            list1 = list1.next
        
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next

if __name__ == "__main__":
    # list1 = [1, 2, 3]
    # list2 = [1, 3, 4]
    list1 = ListNode(1, ListNode(2, ListNode(3)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    
    res = merge_two_lists(list1, list2)
    values = []
    while res:
        values.append(res.val)
        res = res.next

    print(values)
