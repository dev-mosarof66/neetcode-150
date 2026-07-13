class Solution:
    def __init__(self):
        self.bucket = 1000
        self._table = [[] for _ in range(self.bucket)]
        pass

    def hash(self, key: int) -> int:
        return key % self.bucket

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in s:
            index = self.hash(ord(char))
            self._table[index].append(char)

        for char in t:
            index = self.hash(ord(char))
            if char in self._table[index]:
                self._table[index].remove(char)
        
        for bucket in self._table:
            if len(bucket) != 0:
                return False
            
        return True


