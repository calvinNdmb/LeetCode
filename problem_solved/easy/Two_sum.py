import time
start_time = time.time()

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:    
        print (len(nums))   
        for pos, i in enumerate(nums):
            for j in range(pos + 1, len(nums)):
                if i + nums[j] == target:
                    return [pos, j]
    def soluc(self, nums: list[int], target: int) -> list[int]:    
        a = {}
        for pos, i in enumerate(nums):
            complement = target - i
            if complement in a:
                return [a[complement], pos]
            a[i] = pos
        




if __name__ ==  '__main__':
    s=Solution()
    print(s.soluc([10, 20, 30, 40], 50))

    end_time = time.time()
    print(f"elapsed:{end_time-start_time:.10f}")
