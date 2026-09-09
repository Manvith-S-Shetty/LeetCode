class Solution:
    def countCommas(self, n: int) -> int:
        total_comma = 0
        throshold = 1000
        while n>=throshold:
            total_comma += n-throshold +1
            throshold *= 1000
        return total_comma