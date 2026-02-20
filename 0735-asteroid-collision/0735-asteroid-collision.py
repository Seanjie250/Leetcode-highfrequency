class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if asteroids[i] >= 0:
                stack.append(asteroids[i])
            elif asteroids[i] < 0:
                alive = True
                while stack and stack[-1] > 0 :
                    if stack[-1] < - asteroids[i]:
                        stack.pop()
                    elif stack[-1] == - asteroids[i]:
                        stack.pop()
                        alive = False
                        break
                    else:
                        alive = False
                        break
                if alive == True:   
                    stack.append(asteroids[i])
            
                
            i += 1

        return stack
        
                
        