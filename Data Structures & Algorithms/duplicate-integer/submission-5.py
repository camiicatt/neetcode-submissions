from collections import Counter
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if not nums:
            return False
        
        frequency_map = Counter(nums)

        most_frequent, highest = frequency_map.most_common(1)[0]

        if highest > 1:
            return True
        return False