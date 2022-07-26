class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        mp_s = {}
        mp_t = {}
        
        for i in range(len(s)):
            if (s[i] not in mp_s) and (t[i] not in mp_t):
                mp_s[s[i]] = t[i]
                mp_t[t[i]] = s[i]
            elif mp_s.get(s[i]) != t[i] or mp_t.get(t[i]) != s[i]:
                return False
        
        return True

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapST, mapTS = {}, {}

        for c1, c2 in zip(s, t):
            if ((c1 in mapST and mapST[c1] != c2) or \
                (c2 in mapTS and mapTS[c2] != c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True

            