class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        def process_task(idx_task, buckets):
            if idx_task == len(tasks):
                return True
            for i in range(len(buckets)):
                if buckets[i] + tasks[idx_task] <= sessionTime:
                    buckets[i] += tasks[idx_task]
                    if process_task(idx_task + 1, buckets):
                        return True
                    buckets[i] -= tasks[idx_task]
                    if buckets[i] == 0:
                        return False
            return False

        def possible(num_buckets):
            buckets = [0 for _ in range(num_buckets)]
            buckets[0] = tasks[0]
            return process_task(1, buckets)
        
        tasks.sort(reverse=True)
        
        l, r = max(1, sum(tasks) // sessionTime), len(tasks)

        while l < r:
            m = (l + r) // 2
            
            if possible(m):
                r = m
            else:
                l = m + 1

        return l