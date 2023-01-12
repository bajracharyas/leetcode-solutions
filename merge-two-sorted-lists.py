# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged = None
        c = None
        f = list1
        s = list2
        
        while True:
            if f == None and s == None:
                return merged
            elif f == None:
                if merged == None:
                    return s
                else:
                    c.next = s
                    return merged
            elif s == None:
                if merged == None:
                    return f
                else:
                    c.next = f
                    return merged
            else:
                n = ListNode(min(f.val, s.val))
                if f.val < s.val:
                    f = f.next
                else:
                    s = s.next
                if merged == None:
                    merged = n
                    c = n
                else:
                    c.next = n
                    c = c.next
        
        return merged
        