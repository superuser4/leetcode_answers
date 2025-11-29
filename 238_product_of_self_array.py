    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        answer = [1] * arr_len
        
        prefix = 1
        for i in range(arr_len):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(arr_len -1, -1, -1):
            answer[i] *= postfix
            postfix *= nums[i]
        return answer
