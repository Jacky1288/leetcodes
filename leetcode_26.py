"""
标题：删除有序数组中的重复项
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # nums = nums.sort()
        news = set()
        length = len(nums)
        for i in range(0, length):
            if nums[i] not in news:
                news.add(nums[i])

        newnums = list(news)
        print(newnums)
        return len(newnums)

    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


if __name__ == "__main__":
    solution = Solution()
    a = [1, 1, 2]
    b = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates2(a))
    print(a)
    print(solution.removeDuplicates2(b))
    print(b)
