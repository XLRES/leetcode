class Solution:
    def hasCycle(self,head):
        p1 = p2 = head
        p1 = p1.next
        p2 = p2.next.next
        while(p1 != none and p2 != none):
            p1 = p1.next
            p2 = p2.next.next
            if (p1 == p2 ): break
        if p1==p2 : return True
        else return False

