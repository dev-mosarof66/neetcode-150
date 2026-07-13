class Solution:
    def __init__(self):
        self.bucket = 1000
        self.hash_table = [[] for _ in range(self.bucket)]

    def hash(self, key: int) -> int:
        return key % self.bucket
    
    def insert(self, key: int) -> None:
        index = self.hash(key)
        self.hash_table[index].append(key)

    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            index = self.hash(num)
            if num in self.hash_table[index]:
                return True
            self.insert(num)
        return False