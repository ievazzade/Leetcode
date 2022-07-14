class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count_s = {}
        ans = []
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1
        
        for ch in order:
            ans.append(ch * count_s.get(ch, 0))
            count_s[ch] = 0
            
        for ch in count_s:
            ans.append(ch * count_s[ch])
        
        return "".join(ans)