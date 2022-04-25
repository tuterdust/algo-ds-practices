class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def has_cycle(head) -> ListNode:
    if not head:
        return None
    node = head
    visited_dict = {}
    while True:
        if node in visited_dict:
            return node
        visited_dict[node] = True
        if node.next is None:
            return None
        node = node.next
