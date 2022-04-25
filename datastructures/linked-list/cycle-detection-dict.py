class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

def hasCycle(head) -> bool:
    if not head:
        return False
    node = head
    visited_dict = {}
    while True:
        if node in visited_dict:
            return True
        visited_dict[node] = True
        if node.next is None:
            return False
        node = node.next

    # return False
