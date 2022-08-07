class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        "leetcode"
        ["leet", "code"]
        """

        def wb_rec(s, dict, start):
            if start == len(s):
                return True
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in dict and wb_rec(s, dict, end):
                    return True
            
            return False

        return wb_rec(s, wordDict, 0)

    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        "leetcode"
        wordDict = ["leet","code"]
        """
        @lru_cache
        def wordBr_rec(s, wordDict, start):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and wordBr_rec(s, wordDict, end):
                    return True
            return False
        
        return wordBr_rec(s, frozenset(wordDict), 0)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)
        visited = set()
        queue = deque([0])
        
        while queue:
            start = queue.popleft()
            
            if start in visited:
                continue
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    queue.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
            
        return False