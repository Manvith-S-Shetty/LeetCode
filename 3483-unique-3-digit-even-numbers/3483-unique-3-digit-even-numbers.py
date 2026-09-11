from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = Counter(digits)
        res = 0
        for num in range(100,1000,2):
            d1 = num // 100 # to get the hundred
            d2 = (num//10)%10 # to get the tens place
            d3 = num %10 #to get the units place

            total = Counter([d1,d2,d3])
            for digit,count in total.items():
                if counts[digit]<count:
                    break
            else:
                res +=1
        return res