def reverseList(self, head: ListNode) -> ListNode:
    prev_node = None
    curr_node = head
    if head == None:
        return None
    next_node = head.next
    while next_node:
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node
        next_node = curr_node.next
    curr_node.next = prev_node
    return curr_node
