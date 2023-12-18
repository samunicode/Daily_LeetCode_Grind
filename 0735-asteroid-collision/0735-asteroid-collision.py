class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ls = asteroids
        for stone in ls:
            stack.append(stone)
            while len(stack) >= 2 and stack[-1] < 0 and stack[-2] > 0:
                stone1 = stack.pop()
                stone2 = stack.pop()

                if stone2 > abs(stone1): stack.append(stone2)
                if stone2 < abs(stone1): stack.append(stone1)

        return stack
                
                