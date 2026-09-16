class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ind =[]
        i_count = 0
        idx =0
        
        for i in nums:
            j_count = 0
            idx += i_count
            for idx, j in enumerate(nums[i_count+1:], start=i_count + 1):
                if i + j == target:
                    ind = [i_count,idx]
                    return ind
            i_count += 1

        