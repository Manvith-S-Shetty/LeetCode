class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st=[]
        for ast in asteroids:
            is_alive = True
            while st and st[-1]>0 and ast<0:
                if st[-1]<abs(ast):
                    st.pop()
                elif st[-1] == abs(ast):
                    st.pop()
                    is_alive=False
                    break
                else:
                    is_alive = False
                    break
            if is_alive:
                st.append(ast)
        return st
