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
 
 
 class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        "internationa"
                    ^
        "i3rna4al"
               ^
        """
        p1, p2 = 0, 0 
        
        while p1 < len(word) and p2 < len(abbr):
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
            elif abbr[p2] == "0": return False
            
            elif abbr[p2].isnumeric():
                num_str = []
                while p2 < len(abbr) and abbr[p2].isnumeric():
                    num_str.append(abbr[p2])
                    p2 += 1
                num = int("".join(num_str))
                p1 += num
            else:
                return False
        
        return (p1 == len(word)) and (p2 == len(abbr))