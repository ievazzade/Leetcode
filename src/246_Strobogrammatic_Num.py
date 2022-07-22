class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotated_digits = {'0':'0','1':'1','6':'9','8':'8','9':'6'}
        rotated_num_list = []
        
        for c in reversed(num):
            if c in rotated_digits:
                rotated_num_list.append(rotated_digits[c])
            else:
                False
        rotated_num = "".join(rotated_num_list)
        
        return num == rotated_num