class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        hmap, presum, curr = {0: dummy}, 0, head
        while curr != None:
            presum += curr.val
            hmap[presum] = curr
            curr = curr.next
            
        curr = dummy
        presum = 0
        while curr != None:
            presum += curr.val
            curr.next = hmap[presum].next
            curr = curr.next
            
        return dummy.next