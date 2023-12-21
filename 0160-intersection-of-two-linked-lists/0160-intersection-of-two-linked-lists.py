# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        curr, l1 = headA, 0
        while curr.next != None:
            l1 += 1
            curr = curr.next
        tailA, l1 = curr, l1 + 1

        curr, l2 = headB, 0
        while curr.next != None:
            l2 += 1
            curr = curr.next
        tailB, l2 = curr, l2 + 1

        if tailA.val != tailB.val: return None

        else:
            diff = max(l1, l2) - min(l2,l1)
            if l1 >= l2:
                curr = headA
                while diff != 0:
                    curr = curr.next
                    diff -= 1
                ncurr = headB
            elif l1 < l2:
                ncurr = headB
                while diff != 0:
                    ncurr = ncurr.next
                    diff -= 1
                curr = headA

            while curr != None:
                if curr == ncurr:
                    return curr
                    break
                curr = curr.next
                ncurr = ncurr.next
            
            return None


        """
        SOLUTION BY REVERSAL, NOT GETTING ACCEPTED
        """
        # prev, curr = None, headA
        # while curr != None:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp
        
        # headA = prev

        # prev, curr = None, headB
        # while curr != None:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = temp

        # headB = prev

        # curr, ncurr = headA, headB
        # while curr.next.val == ncurr.next.val:
        #     curr = curr.next
        #     ncurr = ncurr.next
        
        # if curr.val == ncurr.val : return ncurr.val
        # else: return None

             
