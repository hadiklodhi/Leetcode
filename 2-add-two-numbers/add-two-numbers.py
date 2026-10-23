# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head1 = l1
        head2 = l2
        
        while l1 and l2:
            l1 = l1.next 
            l2 = l2.next
        if l1:
            l1 = head2
            l2 = head1
        else:
            l1 = head1
            l2 = head2
        head = l2
        count = 0
        while l1 and l2:
            total = l1.val + l2.val + count
            if total >= 10:
                l2.val = total%10
                count = total//10
            else:
                l2.val = total
                count = 0
            prev = l2
            l1 = l1.next 
            l2 = l2.next
        while l2:
            total = l2.val + count
            count = total//10
            l2.val = total%10
            prev = l2
            l2 = l2.next
        if count:
            prev.next = ListNode(count)
        return head


        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        