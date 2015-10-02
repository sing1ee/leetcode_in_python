#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_parts = version1.split('.')
        v2_parts = version2.split('.')
        idx1, idx2, len1, len2 = 0, 0, len(v1_parts), len(v2_parts)
        while idx1 < len1 and idx2 < len2:
            i1 = idx1
            i2 = idx2
            v1, v2 = int(v1_parts[i1]), int(v2_parts[i2])
            if v1 > v2:
                return 1
            if v1 < v2:
                return -1
            idx1 = i1 + 1
            idx2 = i2 + 1
        if idx1 < len1:
            sum = 0
            for i in xrange(idx1, len1):
                sum += int(v1_parts[i])
            return 1 if sum > 0 else 0
        if idx2 < len2:
            sum = 0
            for i in xrange(idx2, len2):
                sum += int(v2_parts[i])
            return -1 if sum > 0 else 0
        return 0


if __name__ == '__main__':
    print Solution().compareVersion('1.0.1', '1')