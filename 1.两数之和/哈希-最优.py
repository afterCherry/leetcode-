# 用哈希表建立原列表中元素值和下标值的对应

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset={}
        for i in range(len(nums)):
            temp=target-nums[i]
            if hashset.get(temp) is not None:
                return [hashset.get(temp),i]
            hashset[nums[i]]=i

# 时间复杂度O（n）—直接比暴力法降低了一次啊
# 空间复杂度O（n）