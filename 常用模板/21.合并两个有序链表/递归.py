# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 先剪枝
        if not l1:
            return l2
        if not l2:
            return l1
        # 进行递归—简单又刺激
        if l1.val<=l2.val:
            # 进行递归还得接上啊，这样最后才能得一条链表
            l1.next=self.mergeTwoLists(l1.next,l2)
            # 递归完了要结果
            return l1 #l1是整个结果链表的表头
        else:
            l2.next=self.mergeTwoLists(l2.next,l1)
            # 递归完了要结果
            return l2 #l1是整个结果链表的表头