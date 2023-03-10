class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for x in range(len(nums)+1):
            for i in itertools.combinations(nums,x):
                res.append(list(i))
        return res