class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 把列表直接搞成所求
        nums.sort(key=lambda x:x==val)
        return len(nums)-nums.count(val) #就是结果长度