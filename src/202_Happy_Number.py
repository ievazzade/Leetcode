class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit * digit
            return total_sum
        
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        
        return n == 1

# Floyd's Cycle-Finding Algorithm
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit * digit
            return total_sum
        
        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        
        return fast == 1