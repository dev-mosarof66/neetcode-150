class Solution:
    def __init__(self):
        self.bucket = 1000
        self._table1 = [[] for _ in range(self.bucket)]
        self._table2 = [[] for _ in range(self.bucket)]
        pass

    def hash(self, key: int) -> int:
        return key % self.bucket

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for char in s:
            index = self.hash(ord(char))
            self._table1[index].append(char)

        for char in t:
            index = self.hash(ord(char))
            self._table2[index].append(char)
        
        if(self._table1 == self._table2):
            return True
        return False

