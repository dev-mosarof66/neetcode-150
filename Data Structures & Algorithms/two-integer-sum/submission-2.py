class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i


        for i in range(0, len(nums)):

            x = target - nums[i]
            if x in dict and i != dict[x]:
                return [i, dict[x]]

        pass
