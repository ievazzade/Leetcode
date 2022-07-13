class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
         0 1 2 3 4 5 6 7 8 9  10 11 12 13 14 15 16 17 18 19 
        "i n t e r n a t i o  n  a  l  i  z  a  t  i  o  n"   m = 20
                                                         ^
         
         0  1   2  3  4  5  6
        "i  1   2  i  z  4  n"  n = 7
                            ^
        i = 19
        j = 6
        k = 6

        """
        i, j = 0, 0
        m, n = len(word), len(abbr)
        
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                # number
                if abbr[j].isnumeric() and int(abbr[j]) == 0: return False
                if abbr[j].isnumeric():
                    k = j
                    while k < n and abbr[k].isnumeric():
                        k += 1
                    i += int(abbr[j:k])
                    j = k
                # string
                else:
                    return False
            
        
        return i == m  and j == n
        