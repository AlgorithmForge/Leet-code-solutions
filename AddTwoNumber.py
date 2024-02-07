class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        # Initialize a dummy node to simplify the handling of the result linked list
        dummy = ListNode()
        # Use current to traverse and build the result list
        current = dummy
        # Initialize carry to 0 to account for any carry generated during addition
        carry = 0

        # Continue iterating until both input linked lists are fully traversed, and there is no carry left to add
        while l1 or l2 or carry:
            # Extract digits from the current nodes or use 0 if one of them is None
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate the sum and carry
            total = x + y + carry
            carry = total // 10

            # Create a new node with the value of total % 10 (to handle cases where the sum is greater than 9)
            current.next = ListNode(total % 10)

            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # Move to the next result node
            current = current.next

        # Return the next node of the dummy node, which is the head of the result linked list
        return dummy.next
