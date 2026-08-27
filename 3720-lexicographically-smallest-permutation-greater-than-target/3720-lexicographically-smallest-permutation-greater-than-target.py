from collections import Counter
#Just Pasted not learnt...!!!!!
class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        count = Counter(s)
        prefix = []

        # Match target from left to right
        i = 0

        while i < len(target) and count[target[i]] > 0:
            count[target[i]] -= 1
            prefix.append(target[i])
            i += 1

        # Try to make the current position bigger first
        if i < len(target):
            for ch in sorted(count):
                if ch > target[i] and count[ch] > 0:
                    count[ch] -= 1

                    suffix = []
                    for c in sorted(count):
                        suffix.append(c * count[c])

                    return ''.join(prefix) + ch + ''.join(suffix)

        # If current position cannot be increased,
        # go backwards and try an earlier position
        for j in range(len(prefix) - 1, -1, -1):

            # Put the previously used character back
            old = prefix.pop()
            count[old] += 1

            for ch in sorted(count):
                if ch > target[j] and count[ch] > 0:
                    count[ch] -= 1

                    suffix = []
                    for c in sorted(count):
                        suffix.append(c * count[c])

                    return ''.join(prefix) + ch + ''.join(suffix)

        return ""