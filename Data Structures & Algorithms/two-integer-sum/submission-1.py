class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,n in enumerate (nums):
            finder = target - n
            if finder in seen:
                return [seen[finder],i]

            seen[n] = i