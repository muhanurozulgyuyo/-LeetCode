class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L_count = 0
        R_count = 0
        count = 0
        
        # while i < len(s):
        #     if s[i] == 'L':
        #         L_count += 1
        
        for i in range(len(s)):
            if L_count > 0 and R_count > 0:
                if L_count == R_count:
                    count += 1
                    if s[i] == 'L':
                        L_count += 1
                    else:
                        R_count += 1
                else:
                    if s[i] == 'L':
                        L_count += 1
                    else:
                        R_count += 1                    
            else:
                if s[i] == 'L':
                    L_count += 1
                else:
                    R_count += 1
                
        return count + 1