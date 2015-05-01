class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        h = ListNode(0)
        h.next = head
        p1 = p2 = head.next
        for i in range(n):
            p1 = p1.next
        while (p1.next != None):
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return  h.next

s = Solution()
head = ListNode(0)
p = head
for i in range(1,6):
    p.next = ListNode(i)
    p = p.next
p = head;
while (p != None):
    print p.val,
    p = p.next
head = s.removeNthFromEnd(head, 3)
p = head
while (p != None):
    print p.val,
    p = p.next
    
