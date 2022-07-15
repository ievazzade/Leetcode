class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for s in strings:
            key = tuple((ord(c) - ord(s[0])) % 26 for c in s)
            mp[key].append(s)
        return mp.values()