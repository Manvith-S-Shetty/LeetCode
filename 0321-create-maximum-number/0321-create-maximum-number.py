class Solution:
    def maxNumber(self, nums1, nums2, k):

        # Get the largest subsequence of length `need`
        def max_subsequence(nums, need):
            remove = len(nums) - need
            st = []

            for x in nums:
                # Remove smaller digits if we are allowed to remove them
                while st and remove > 0 and st[-1] < x:
                    st.pop()
                    remove -= 1

                st.append(x)

            return st[:need]

        # Merge two subsequences into the largest possible sequence
        def merge(a, b):
            result = []
            i = 0
            j = 0

            while i < len(a) or j < len(b):

                # If one array is finished, take from the other
                if i == len(a):
                    result.append(b[j])
                    j += 1

                elif j == len(b):
                    result.append(a[i])
                    i += 1

                # Choose the sequence that is lexicographically larger
                elif a[i:] > b[j:]:
                    result.append(a[i])
                    i += 1

                else:
                    result.append(b[j])
                    j += 1

            return result

        best = []

        # Try every possible split of k digits
        for x in range(k + 1):
            y = k - x

            # This split is impossible
            if x > len(nums1) or y > len(nums2):
                continue

            a = max_subsequence(nums1, x)
            b = max_subsequence(nums2, y)

            candidate = merge(a, b)

            # Keep the largest candidate
            if candidate > best:
                best = candidate

        return best