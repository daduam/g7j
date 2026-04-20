class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for asteroid in asteroids:
            shouldappend = True
            while st and st[-1] > 0 and asteroid < 0:
                if abs(asteroid) > st[-1]:
                    st.pop()
                elif abs(asteroid) == st[-1]:
                    st.pop()
                    shouldappend = False
                    break
                else:
                    shouldappend = False
                    break
            if shouldappend:
                st.append(asteroid)
        return st