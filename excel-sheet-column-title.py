#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):

    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        chars = [chr(i) for i in range(64, 91)]  # A is 65
        chars[0] = 'Z'
        ret = n / 26
        rem = n % 26

        rl = ''

        while ret > 0 or rem > 0:
            rl = '%s%s' % (chars[rem], rl)
            if 1 == ret and 0 == rem:
                break
            if 0 == rem:
                ret -= 1
            rem = ret % 26
            ret /= 26
        return rl
if __name__ == '__main__':
    print Solution().convertToTitle(1326)