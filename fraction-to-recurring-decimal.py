#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """

        if 0 == numerator:
            return '0'

        fraction, pos = [], 0

        if numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1
        elif numerator < 0:
            numerator *= -1
            pos += 1
            fraction.append('-')
        elif denominator < 0:
            denominator *= -1
            pos += 1
            fraction.append('-')

        ret = numerator / denominator
        remainder = numerator % denominator

        fraction.append(str(ret))
        if not remainder:
            return ''.join(fraction)
        else:
            fraction.append('.')
        remainder_pos = {}
        pos += 1
        while remainder:
            pos += 1
            t = remainder * 10
            rt = t / denominator
            remainder = t % denominator
            if remainder in remainder_pos:
                if str(rt) == fraction[remainder_pos[remainder]]:
                    return '%s(%s)' % (''.join(fraction[:remainder_pos[remainder]]),
                                       ''.join(fraction[remainder_pos[remainder]:]))
            remainder_pos[remainder] = pos
            fraction.append(str(rt))
        return ''.join(fraction)


if __name__ == '__main__':
    print Solution().fractionToDecimal(-7, 12)