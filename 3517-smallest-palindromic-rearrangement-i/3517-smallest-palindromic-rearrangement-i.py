from collections import Counter
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq=Counter(s) # make a count of the ""
        left=[]
        middle="" # store odd ones
        for ch in sorted(freq):
            left.append(ch*(freq[ch]//2)) #make the character freq half we get left
            if freq[ch]%2==1:
                middle=ch
        left="".join(left)
        return left+middle+left[::-1]