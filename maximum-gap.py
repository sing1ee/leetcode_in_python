#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        num_strs = []
        max_size = 1
        for s in num:
            num_strs.append(str(s)[::-1])
            max_size = max(max_size, len(str(s)))
        for i in range(max_size):
            buckets = [[] for j in range(10)]
            for s in num_strs:
                if len(s) <= i:
                    buckets[0].append(s)
                else:
                    buckets[int(s[i])].append(s)
            num_strs = []
            for j in range(10):
                num_strs.extend(buckets[j])
            print num_strs
        num = [int(x[::-1]) for x in num_strs]
        max_gap = 0
        for x in range(len(num) - 1):
            max_gap = max(max_gap, num[x + 1] - num[x])
        return max_gap


if __name__ == '__main__':
    print Solution().maximumGap([1,21,0])