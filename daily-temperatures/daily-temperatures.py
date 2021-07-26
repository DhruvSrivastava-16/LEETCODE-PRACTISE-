class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)

        ans = [0] * length

        stack = []

        for i in range(length - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            
            if stack and T[i] < T[stack[-1]]:
                ans[i] = stack[-1] - i

            stack.append(i)

        return ans