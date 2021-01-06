class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 虚拟结点dummy保存第一个结点，最后用来返回
        dummy=ListNode(-1) #也可以理解为哨兵结点
        # 遍历来形成链表
        prev=dummy
        # 对两个链表的公共部分
        while l1 and l2:
            if l1.val<=l2.val:
                prev.next=l1
                l1=l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        # 最后有一个链表有剩余，则直接拼接到结果链表上—两个if只会执行一个
        if l1:
            prev.next=l1
        if l2:
            prev.next = l2
        # 由两个if只会执行一个来看，则又可以使用 if else 一行代码了
        # prev.next=l1 if l1 is not None else l2
        return dummy.next


