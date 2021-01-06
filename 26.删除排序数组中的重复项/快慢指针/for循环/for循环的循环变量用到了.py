# 最终结果是逻辑上的

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        length=len(nums)
        for j in range(1,length):
            # 不相等开始换，j是一直在走
            if nums[i]!=nums[j]:
                i+=1
                # 这里交换、赋值都可以的
                nums[i],nums[j]=nums[j],nums[i]
        return i+1

