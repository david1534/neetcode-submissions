class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_map = {}
        for n in nums:
            if n not in my_map:
                my_map[n] = 1
            else:
                return True
        return False
            