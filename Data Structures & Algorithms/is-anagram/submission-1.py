class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_table1 = {}
        hash_table2 = {}
        count = 1
        for i in s:
            if i in hash_table1:
                hash_table1[i] += 1
            else:
                hash_table1[i] = 1
        for j in t:
            if j in hash_table2:
                hash_table2[j] += 1
            else:
                hash_table2[j] = 1
        if hash_table1 == hash_table2:
            return True
        else:
            return False
                

        