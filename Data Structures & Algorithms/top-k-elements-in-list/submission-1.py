class Solution:
      def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict = {}

        for num in nums:

            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        dict = {
            k: v
            for k, v in sorted(dict.items(), key=lambda item: item[1],reverse=True)
        }

        print(dict)

        sol = list(dict.keys())[:k]
        return sol


