class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        soln = [[]]

        for num in nums:
            soln += [lst + [num] for lst in soln]
        return soln