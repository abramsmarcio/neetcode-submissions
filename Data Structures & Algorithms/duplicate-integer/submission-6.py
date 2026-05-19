class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for i in range(len(nums)):
            if nums[i] in hash_table.values():
                return True
            hash_table[i] = nums[i]
        return False
 
        