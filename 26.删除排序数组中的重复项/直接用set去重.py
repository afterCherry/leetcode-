class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # set 之后元素可能不是从小到大排序的，所以加sorted()—实现正数负数一起的从小到大排序
        # nums[:] 是在原地修改列表
        # nums=list(sorted(set(nums))) 是nums表示新得到的列表
        nums[:]=list(sorted(set(nums)))
        return len(nums)