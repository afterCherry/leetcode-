class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length=len(nums)
        if target in nums:
            return nums.index(target)
        # 剪枝
        if target<nums[0]:
            return 0
        if target > nums[length-1]:
            return length
        else:
            i=0
            while i<len(nums):
                if target>nums[i]:
                    i+=1
                else:
                    return i

        # 对列表遍历除了上面的用下标，也可以直接用列表的元素
        # for item in nums:
        #     if target<item:
        #         return nums.index(item)