class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        nge={}
        for num in nums2:
            while st and st[-1]<num:
                smaller = st.pop()
                nge[smaller]=num
            st.append(num)
        while st:
            nge[st.pop()]=-1
        ans=[]
        for num in nums1:
            ans.append(nge[num])
        return ans
