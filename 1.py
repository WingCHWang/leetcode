#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def twoSum(self, nums, target):
        num2index = {}
        for index, num in enumerate(nums):
            if num not in num2index:
                num2index[num] = []
            num2index[num].append(index)
        for num, index in num2index.items():
            other = target - num
            if other in num2index:
                if other == num:
                    if len(index) >= 2:
                        return index[:2]
                else:
                    return [index[0], num2index[other][0]]
        return []


