from typing import Optional


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

    def __str__(self):
        head = self
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return str(vals)

    def __len__(self):
        head = self
        count = 0
        while head:
            count += 1
            head = head.next
        return count

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        phead, cur = ListNode(0, head), head
        prev = phead
        while(cur):
            if not cur.next:
                np, nn = None, None
            elif not cur.next.next:
                np, nn = cur.next, None
            else:
                np, nn = cur.next, cur.next.next

            prev.next, cur.next = cur.next, prev
            prev, cur = np, nn
        return phead.next

s = Solution()
print(s.swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
