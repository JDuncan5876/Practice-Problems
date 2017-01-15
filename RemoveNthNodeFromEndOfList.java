/**
 * Given a linked list, remove the nth node from the end of list and return its head.
 * @author Jared Duncan
 */
public class RemoveNthNodeFromEndOfList {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode a = head;
        ListNode b = head;
        for (int i = 0; i < n; i++) {
            b = b.next;
        }
        if (b == null) {
            return head.next;
        }
        while (b.next != null) {
            a = a.next;
            b = b.next;
        }
        a.next = a.next.next;
        return head;
    }
}

/*
 * Given definition of ListNode
 */
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}