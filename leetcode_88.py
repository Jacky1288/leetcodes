from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 补齐内容
        nums1[m:] = nums2[:n]
        # 排序
        nums1.sort()




