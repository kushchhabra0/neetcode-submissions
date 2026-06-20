class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for a in asteroids:
            # COLLISION CONDITION:
            # Takraav tabhi hoga jab stack ka top asteroid RIGHT ja raha ho (stack[-1] > 0)
            # AUR naya incoming asteroid LEFT ja raha ho (a < 0).
            while stack and a < 0 and stack[-1] > 0:
                diff = a + stack[-1]
                
                if diff < 0:
                    # 1. Incoming bada hai: Stack wale ko udaao aur loop chalne do (incoming survived)
                    stack.pop()
                    continue
                elif diff > 0:
                    # 2. Stack wala bada hai: Incoming khatam ho gaya. Loop break karo.
                    break
                else:
                    # 3. Dono barabar hain: Dono ek dusre ko uda denge. Stack pop karo aur loop break karo.
                    stack.pop()
                    break
            else:
                # (Python for-else):
                # Yeh 'else' block tabhi chalega jab upar wala 'while' loop APNE AAP bina kisi 'break' ke khatam hua ho!
                # Matlab incoming asteroid ya toh sabko pop karke jeet gaya, ya koi collision hi nahi hui.
                # Aise me ise safely stack me push kar do.
                stack.append(a)
        
        return stack