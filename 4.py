#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        size1 = len(nums1)
        size2 = len(nums2)

        target = (size1 + size2 + 1) // 2

        index1 = 0
        index2 = 0

        is_odd = (size1 + size2) % 2 != 0

        while index1 < size1 and index2 < size2:
            # print(l1, l2)
            # print(target)
            if target == 1:
                break
            half_target = target // 2
            t1 = index1 + half_target - 1
            t2 = index2 + half_target - 1
            t1 = t1 if t1 < size1 else size1 - 1
            t2 = t2 if t2 < size2 else size2 - 1
            if nums1[t1] == nums2[t2]:
                target -= t1 - index1 + 1
                index1 = t1 + 1
                target -= t2 - index2
                index2 = t2
            elif nums1[t1] < nums2[t2]:
                target -= t1 - index1 + 1
                index1 = t1 + 1
            else:
                target -= t2 - index2 + 1
                index2 = t2 + 1

        # print(index1, index2, target)
        if index1 == size1:
            index2 += target - 1
        elif index2 == size2:
            index1 += target - 1
        top2 = list(sorted(nums1[index1:index1 + 2] + nums2[index2:index2 + 2]))[:2]
        if is_odd:
            return top2[0]
        else:
            return (top2[0] + top2[1]) / 2


if __name__ == "__main__":
    s = Solution()
    # print(s.findMedianSortedArrays([7, 8, 9], [1, 2, 3, 4, 5, 6, 10]))
    # print(s.findMedianSortedArrays([2], [1, 3, 4]))
    # print(s.findMedianSortedArrays([1], [2, 3, 4]))
    print(s.findMedianSortedArrays([3, -1, 3], [-2]))
    # print(s.findMedianSortedArrays([1, 2], [-1, 3]))
    # print(s.findMedianSortedArrays([1, 2], [3, 4]))
    # print(s.findMedianSortedArrays([i for i in range(100)], [i for i in range(2, 100, 3)]))
    # print(list(sorted([i for i in range(100)] + [i for i in range(2, 100, 3)]))[67])
