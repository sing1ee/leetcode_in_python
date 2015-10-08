###Maximum Gap

####题目

给定一个未排序的数组，找到该数组在排序形式下，连续两个数字相减得到差的最大值。

尽可能找到一个满足线性的时间和空间复杂度的方法。

如果数组中元素个数少于2个，则返回0。

给定假设：数组中所有的元素都是非负的整数，4字节。


####分析

这个题目在LeetCode中归类到Hard组，就是比较难的。但其实做下来，也并不觉得难。也是对基本算法的掌握、理解。

看到这个题目，第一反应是要排序，这样再遍历一遍，就得到了想要的值。那怎么排序呢？如果没有要求***尽可能找到一个满足线性的时间和空间复杂度的方法***，直接选择某一种排序算法，然后遍历一遍即可，其实这样也可以通过LeetCode，大家可以试试，Python的sorted函数的算法是TimeSort，大家可以看链接：https://en.wikipedia.org/wiki/Timsort，其平均时间复杂度是O(nlogn)的，空间O(n)的，只不过最差情况也是O(nlogn)，最好的情况是O(n)，这里的比快排好些。

但如果要求线性的时间和空间复杂度的话，情况就不一样了。其实，也有几个线性时间的排序算法的：

1. 计数排序：适合小范围的整数，浮点数不要考虑了，是一种稳定的排序算法，这里的稳定是指排序后的相同值的元素原有的相对位置不会发生改变。
2. 基数排序：同样适用于整数，不过范围可以很大，可以对一些位数有限的十进制数排序（例如本题）。
3. 桶排序：待排序的数据必须在某一个范围内，可以对浮点数进行排序。

这几个排序算法的应用场景并不多，但确实很有用：基数排序可以用于后缀数组的倍增算法，使时间复杂度从O(nlognlogn)降到O(n*logn)，学习过后缀树组的童鞋，一定深有体会。

在我们这个题目中，我们尝试下基数排序。题目中给定***数组中所有的元素都是非负的整数，4字节***，也就是我们将对一批数位有限的正整数进行排序。基数排序改如何运用呢？先看代码。

```python
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
        num = [int(x[::-1]) for x in num_strs]
        max_gap = 0
        for x in range(len(num) - 1):
            max_gap = max(max_gap, num[x + 1] - num[x])
        return max_gap


if __name__ == '__main__':
    print Solution().maximumGap([1,21,0])

```


代码比较简洁，有几个地方需要注意下：

1. str(s)[::-1] 这是python反转字符串的小技巧
2. max_size保存了数组里数字的最长位数
3. 反转是为了实现方便，基数排序从最低位开始比较，反转之后，就是从0开始。
4. num = [int(x[::-1]) for x in num_strs] 列表推导式的一个应用

上面的代码，找几个例子，简单走几遍，就了然了。

