class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for index_rev in range(len(nums)-1,0,-1):
            if nums[index_rev]==nums[index_rev-1]:
                nums.pop(index_rev)
        return len(nums)