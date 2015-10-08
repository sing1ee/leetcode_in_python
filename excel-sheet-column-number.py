#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = [chr(i) for i in range(65, 91)]  # A is 65
        a_to_i = dict([(chr(i), i - 64) for i in range(65, 91)])
        num, pos = 0, 0
        if 1 == len(s):
            return a_to_i[s]
        for w in s[::-1]:
            num += a_to_i[w] * (26 ** pos)
            pos += 1
        return num

if __name__ == '__main__':
    print Solution().titleToNumber('CVZ')