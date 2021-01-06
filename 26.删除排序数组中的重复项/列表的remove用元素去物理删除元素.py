class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for item in nums[:]:
            if nums.count(item)>1:
                nums.remove(item)
        return len(nums)
