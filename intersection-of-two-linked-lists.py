#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def getIntersectionNode(self, head_a, head_b):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not head_a or not head_b:
            return None
        len_a, len_b, next_a, next_b = 0, 0, head_a, head_b

        while next_a:
            len_a += 1
            next_a = next_a.next

        while next_b:
            len_b += 1
            next_b = next_b.next

        next_a, next_b, len_l = head_a, head_b, 0

        if len_a > len_b:
            len_l = len_b
            for i in xrange(len_a - len_b):
                next_a = next_a.next
        elif len_b > len_a:
            len_l = len_a
            for i in xrange(len_b - len_a):
                next_b = next_b.next
        else:
            len_l = len_a

        # for i in xrange(len_l):
        #     if next_a == next_b and next_a.val == next_b.val:
        #         return next_a
        #     next_a = next_a.next
        #     next_b = next_b.next

        for i in xrange(len_l):
            next_ai = next_a
            next_bi = next_b
            if next_ai == next_bi and next_ai.val == next_bi.val:
                return next_ai
            next_a = next_ai.next
            next_b = next_bi.next

        return None


if __name__ == '__main__':
    head_a = ListNode(1)
    head_b = head_a
    print Solution().getIntersectionNode(head_a, head_b).val