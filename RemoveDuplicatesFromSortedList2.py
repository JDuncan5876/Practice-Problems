# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        newHead = None
        newNode = None
        node = head
        while node:
            if not node.next or node.val != node.next.val:
                if not newHead:
                    newHead = node
                    newNode = newHead
                else:
                    newNode.next = node
                    newNode = newNode.next
                node = node.next
            else:
                val = node.val
                while node and node.val == val:
                    node = node.next
        if newNode: newNode.next = None
        return newHead