class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for item in nums[:]:
            if item==val:
                del item
                return Solution().removeElement(nums,val)
        return len(nums)