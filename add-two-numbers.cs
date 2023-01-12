/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2, int carryOver = 0) {
        int sum = l1.val + l2.val + carryOver;
        int curNodeVal = sum % 10;
        carryOver = sum / 10;
        ListNode retListNode = new ListNode(curNodeVal);
        
        if (l1.next != null || l2.next != null || carryOver != 0) {
            retListNode.next = AddTwoNumbers(l1.next ?? new ListNode(), l2.next ?? new ListNode(), carryOver);
        }
        return retListNode;
    }
}