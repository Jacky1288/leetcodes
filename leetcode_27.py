from typing import List

"""在这段代码中，从后向前遍历列表nums的原因是，我们正在修改列表（通过pop方法删除元素）。如果我们从前向后遍历并删除元素，那么在遍历过程中，列表的长度会改变，可能会导致索引错误或者遗漏某些元素。  例如，假设我们有一个列表[
3, 2, 2, 3]，我们想要删除所有的2。如果我们从前向后遍历，当我们删除第一个2后，列表变为[3, 2, 3]，然后我们移动到下一个索引，跳过了第二个2。  
但是，如果我们从后向前遍历，即使我们删除了元素，也不会影响我们还未遍历到的元素。因此，我们可以安全地修改列表，而不会错过任何元素。 """


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 从后往前遍历
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
