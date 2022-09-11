class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def backTrack(index, prev, cur, value, s):
            if index == n:
                if value == target and cur == 0:
                    ans.append(s)
                return
            
            cur = cur * 10 + int(num[index])
            
            if cur > 0:
                backTrack(index + 1 , prev, cur, value, s)
            
            if not s:
                backTrack(index + 1 , cur, 0, value + cur, str(cur))
            else:
                backTrack(index + 1 , cur, 0, value + cur, s+"+"+str(cur))
                backTrack(index + 1 , -cur, 0, value - cur, s+"-"+str(cur))
                backTrack(index + 1 , prev * cur, 0, value - prev + prev * cur, s+"*"+str(cur))
        
        
        n = len(num)
        ans = []
        backTrack(0,0,0,0,"")
        
        return ans