#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        flag = 0
        cur1 = l1
        cur2 = l2
        _sum = cur1.val + cur2.val
        flag = _sum // 10
        l_sum = ListNode(_sum - flag * 10)
        l_cur = l_sum
        while True:
            if cur1 is not None:
                cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next
            if cur1 is None and cur2 is None:
                break
            if cur1 is None:
                v1 = 0
            else:
                v1 = cur1.val
            if cur2 is None:
                v2 = 0
            else:
                v2 = cur2.val

            _sum = v1 + v2 + flag
            flag = _sum // 10
            l_cur.next = ListNode(_sum - flag * 10)
            l_cur = l_cur.next
        if flag == 1:
            l_cur.next = ListNode(1)
        return l_sum
