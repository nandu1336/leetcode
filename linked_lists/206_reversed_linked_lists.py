from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverese_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, cur = None, head

    while cur: 
        nxt, cur.next = cur.next, prev
        prev, cur = cur, nxt 

    return prev


if __name__ == "__main__":
    # head = [1,2,3,4,5]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    res = reverese_list(head)
    
    while res:
        print(res.val)
        res = res.next
