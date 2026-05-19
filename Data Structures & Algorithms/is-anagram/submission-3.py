class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash_table1 = {}
        for i in s:
            if i in hash_table1:
                hash_table1[i] += 1
            else:
                hash_table1[i] = 1
        for j in t:
            if j in hash_table1:
                hash_table1[j] -= 1
                if hash_table1[j] < 0:
                    return False
            else:
                return False
        return True
            
                

        