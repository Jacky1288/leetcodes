"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。
示例 1：

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        slow = fast = 2
        while fast < n:
            if nums[slow - 2] != nums[fast]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


if __name__ == "__main__":
    solution = Solution()
    a = [1, 1, 1, 1, 2, 2, 2, 3]
    b = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5]
    c = [1, 2, 3, 4, 5]
    i = solution.removeDuplicates(c)
    print(i)
    print(c)
