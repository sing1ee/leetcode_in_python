###Fraction to Recurring Decimal

####题目

给定两个整数，一个作为分子，一个作为分母。请用字符串来表示其对应的浮点数。

如果小数的部分有重复的，就将重复的部分用括号括起来。

举例：

1. 分子为1，分母为2，返回“0.5”
2. 分子为2，分母为1，返回“1”
3. 分子为2，分母为3，返回“0.(6)”

####题目分析

这个题目是LeetCode难度为中等的一个题目，不算难，但是细节挺多的。要想顺利通过，也不容易。接下来，我们就好好分析一下，希望能够帮助到大家。

我们分两种情况考虑，有限小数和无限循环小数。有同学会问无限不循环小数为什么不考虑么？那样你要问问自己，无限不循环小数，对应的分数是多少呢？例如：π=3.14159265358979323846...

第一种情况，有限小数。比较好办，用分子除以分母，得到的商算作一位，然后用余数继续作为分子，除以分母...循环前面的操作，直到余数为0，小数就得到了。

麻烦的是第二种情况，无限循环小数。我们得找到哪一部分是循环的部分。怎么找呢？大家有纸笔的话，可以画画除法的竖式，根据第一种情况的做法，每次都将余数作为新的分子，再进行除法运算。那其实很明朗了，就是只要我记录下出现某一个余数，以及对应的小数的位置，每次得到新的余数就判断是否重复出现。重复出现，还需要考虑一些细节，我们代码过后讲，那么找到循环部分了。

看看代码吧，更直接一些：

```python 

#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

```

代码略长，我来简单解释下：

1. 要考虑分子分母正负的情况，以及-7/5 和 -(7/5) 的不同，比如在Python里，这两个值分别为-2, -1
2. remainder_pos记录余数对应的小数的位置，pos记录当前考虑到哪一位
3. remainder_pos不仅为了判断是否有循环部分，更是为了方便用()将循环部分包含
4. 还要考虑，余数是相同了，但是商不同。。。比如1/6

基本上就这些内容，大家可以看看，还有什么可以提升的地方么？

