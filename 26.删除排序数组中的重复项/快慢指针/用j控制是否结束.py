# 快慢指针用元素赋值
# 最终结果是逻辑上的

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length=len(nums)
        i,j=0,1
        # 快慢指针只用快指针<length就行
        while j<length:
            # 这里的！=更具体是<
            if nums[i]!=nums[j]:
                i += 1
                # 是直接赋值啊！虽然交换很好用但不是交换
                nums[i]=nums[j]
            # i,j都从首元素开始往后走，则两个相等，j往后走
            else:
                j+=1
        return i+1
