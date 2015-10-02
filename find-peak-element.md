###Find Peak Element[LeetCode]

####原题

给定一个数组：num，满足num[i] != num[i+1]。在数组中，找到一个这样的数：它大于其左右的数，请返回这个数所在的位置（这样的数成为peak element）。

这样的数可能有多个，这里只要返回其中一个即可。

同时，可以假设：num[-1] = num[n] = -∞

举例：[1, 2, 3, 1]，3就是要找的数，并且是数组的第2个元素（从0开始），则返回2即可。


####分析

这个题目和待字闺中很早之前的一个题目类似，那个题目好像是找一个小于左右的数。思路想来差不多。我们重新分析一下这个题目：

首先，这样的数存在么？很显然，有了两个条件：

* num[i] != num[i+1]
* num[-1] = num[n] = -∞

这样的数，是一定存在的。要证明很简单，我们不妨假设不存在，那么num[1]，num[0]一定满足num[1] > num[0]。依此类推，num[2] > num[1] ... 一直到num[n] > num[n-1]，就是 -∞ > num[n-1]。那剩下的，不用多说了，同学也不必钻到角落里出不来。

那一定存在这样数，怎么找出来呢？我们先考虑题目中的要求，找到一个即可。怎么找呢？最直接想法，遍历一遍即可。复杂度O(n)，如果仅仅是这样，大家也觉得没意思。如何能更快呢？再快一些的时间复杂度是O(log(n))。熟练的同学，很快意识到，就是二分查找。二分查找可以么？我们不妨试试，走一走这个过程。

首先，我们得到num[mid],mid = (left + right) / 2， left, right的初始是0， n-1。

num[mid]有几种情况呢？

1. num[mid]如果大于num[mid-1]，且大于num[mid+1]。可以直接返回mid了
2. 那剩下的可可能性有: 
	1. num[mid - 1] > num[mid] > num[mid + 1]，考虑左边部分
	2. num[mid - 1] > num[mid] < num[mid + 1]，考虑哪一边都可以
	3. num[mid - 1] < num[mid] < num[mid + 1]，考虑有边部分
3. 上面三种情况，都可以得到结果，原因不妨用上面，我们证明这个数一定存在的思路，反证一下即可。

二分查找的代码不好写，边界处理不好总会有异常情况。理清思路，注意边界，特殊情况自己走两遍。二分查找的变体挺多的，只要明确了可以用二分来试试，基本走几个例子，就可以了。更重要的，还是保证程序的正确性。加油。



####代码

```python


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


```
