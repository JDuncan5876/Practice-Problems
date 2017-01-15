/**
 * Given a sorted linked list, delete all duplicates such that each element appear only once.
 *
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class RemoveDuplicatesFromSortedList {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode repStart = head;
        while (repStart != null) {
            ListNode node = repStart.next;
            while (node != null && node.val == repStart.val) {
                repStart.next = node.next;
                node = repStart.next;
            }
            repStart = node;
        }
        return head;
    }
}