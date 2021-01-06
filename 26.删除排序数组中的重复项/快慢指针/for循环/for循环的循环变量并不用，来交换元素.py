# 最终结果是逻辑上的

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        length=len(nums)
        for item in range(length):
            # 不相等开始换，j是一直在走
            if nums[i]!=nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1

