# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 获取链表个数
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        # 删除第length-n+1个节点
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        for _ in range(length - n):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next