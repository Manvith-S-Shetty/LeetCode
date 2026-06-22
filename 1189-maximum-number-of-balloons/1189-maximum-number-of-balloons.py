from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=Counter(text)
        return min(c['b'],
                    c['a'],
                    c['l']//2,
                    c['o']//2,
                    c['n'])
    '''#remeber the tric is simple BALLO0N B-1 A-1 L-2 O-2 N-1
    if you got questions like 
    How many times can I build a word?
    How many groups can I form?
    How many copies can I make?
    use same tric and COUNT THE GIVEN AND TAKE MINIMUM '''
    
