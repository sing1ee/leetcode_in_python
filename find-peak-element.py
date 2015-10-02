#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            l, r = left, right
            mid = (l + r) / 2
            if mid - 1 < l:
                if mid + 1 > r or nums[mid] > nums[mid + 1]:
                    return mid
                l = mid + 1
            elif nums[mid] < nums[mid - 1]:
                r = mid
            else:
                l = mid
            left, right = l, r


if __name__ == '__main__':
    print Solution().findPeakElement([1, 2, 3, 1])
    print Solution().findPeakElement([1, 2, 3, 4])
    print Solution().findPeakElement([4, 2, 3, 1])
    print Solution().findPeakElement([1, 2, 3, 1])