# 快慢指针用元素直接弹出pop()—O(n),最后的列表即为所求
# pop可以pop(i)也可以pop(j)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,1
        # 【注意】列表的长度是在变化的，所以不能用固定住的length=len(初始化的列表)
        while j<len(nums):
            if nums[i]==nums[j]:
                nums.pop(i)
            j += 1
            i += 1
        # 最后的列表即为所求
        return len(nums)
