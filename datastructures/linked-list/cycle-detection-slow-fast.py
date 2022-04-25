class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def has_cycle(head) -> bool:
    if not head:
        return False

    slow_ptr = head
    fast_ptr = head

    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr is fast_ptr:
            return True

    return False
