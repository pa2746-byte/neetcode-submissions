class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        kv = {}

        for i, n in enumerate(nums):

            diff = target - n
            if diff in kv and kv[diff]!=i:
                if (i<kv[diff]):
                    return [i, kv[diff]]
                else:
                    return [kv[diff],i]
            kv[n]=i

        return []
        