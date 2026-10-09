class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                # Each '(' needs two ')'
                open_needed += 2
                i += 1
            else:
                # We found a ')'
                # Check if it's followed by another ')' to form a pair '))'
                if i + 1 < n and s[i+1] == ')':
                    open_needed -= 2
                    i += 2  # Correctly skip the second ')'
                else:
                    # Single ')' found, we must insert one ')' to make it a pair
                    insertions += 1
                    open_needed -= 2
                    i += 1
                
                # If we have more ')' than matching '('
                if open_needed < 0:
                    insertions += 1  # Insert a '('
                    open_needed += 2 # Balance the count
                    
        return insertions + open_needed
