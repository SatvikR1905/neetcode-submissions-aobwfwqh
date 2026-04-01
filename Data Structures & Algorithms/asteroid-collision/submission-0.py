class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            while stack and num < 0 and stack[-1] > 0:
                b = stack.pop()
                if abs(b) == abs(num):
                    break
                elif abs(b) > abs(num):
                    stack.append(b)
                    break
            else:
                stack.append(num)
        return stack
        