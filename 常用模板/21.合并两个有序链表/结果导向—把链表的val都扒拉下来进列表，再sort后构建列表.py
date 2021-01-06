class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res=[]
        while l1:
            res.append(l1.val)
            l1=l1.next
        while l2:
            res.append(l2.val)
            l2=l2.next
        # 这个程序就靠它了
        res.sort()

        dummy=ListNode(-1)
        prev=dummy
        for item in res:
            node=ListNode(item) #直接就用val造了个结点啊!
            prev.next=node
            prev=prev.next
        return dummy.next
