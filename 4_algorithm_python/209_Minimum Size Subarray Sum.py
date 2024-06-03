class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = sum = 0
        for n in nums:
            sum += n
        if sum < target:
            return 0
        sum = 0
        answer = pow(10, 5)
        while j <= len(nums):
            if sum < target:
                if j != len(nums):
                    sum += nums[j]
                j += 1
            else:
                answer = min(answer, j - i)
                sum -= nums[i]
                i += 1
        return answer