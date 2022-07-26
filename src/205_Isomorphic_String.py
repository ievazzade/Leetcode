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