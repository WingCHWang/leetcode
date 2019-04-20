#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        pre_index_table = {}
        max_len = 0
        pre_left = -2   
        # max_str = ""
        for index, char in enumerate(s):
            pre_index = pre_index_table.get(char, -1)

            if pre_index > pre_left:
                pre_left = pre_index
            cur_len = index - pre_left
            pre_index_table[char] = index
            if cur_len > max_len:
                max_len = cur_len
        str_len = len(s)
        tmp = str_len - pre_left - 1
        if tmp > max_len:
            max_len = tmp
        return max_len


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("ohomm"))
    print(solution.lengthOfLongestSubstring("bwf"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("cdd"))
