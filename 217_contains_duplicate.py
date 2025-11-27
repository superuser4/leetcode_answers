class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)- i) :
                if nums[i] == nums[j]:
                    count += 1
            if count > 1:
                return True
        return False
