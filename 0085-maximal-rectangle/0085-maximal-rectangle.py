class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        col = len(matrix[0])
        max_area = 0
        high = [0]* (col+1)
        for row in matrix:
            for i in range(col):
                high[i] = high[i] + 1 if row[i] == "1" else 0
            st=[-1]
            for i in range(len(high)):
                while high[i] < high[st[-1]]:
                    h = high[st.pop()]
                    w = i - st[-1] - 1
                    max_area=max(max_area,h*w)
                st.append(i)
        return max_area
