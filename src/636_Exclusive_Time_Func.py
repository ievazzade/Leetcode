class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
                                                           ^
        func_id = 0
        type =  e
        timestamp =  7
        
        stack = []
        exclusive_times = [7]
        prev_start_time = 8
        
        
        if start:
            update last function call time
        else: # end
            index(pop from stack) and update time (timestamp - prev_start_time + 1)
            update prev_start_time
            
        """
        
        stack = []
        exclusive_times = [0] * n
        prev_start_time = 0
        
        for log in logs:
            func_id, log_type, timestamp = log.split(":")
            func_id, timestamp = int(func_id), int(timestamp)
            if log_type == "start":
                if stack:
                    exclusive_times[stack[-1]] += timestamp - prev_start_time
                    prev_start_time = timestamp
                stack.append(func_id)
            else:
                exclusive_times[stack.pop()] += timestamp  - prev_start_time + 1
                prev_start_time = timestamp + 1
        
        return exclusive_times
                