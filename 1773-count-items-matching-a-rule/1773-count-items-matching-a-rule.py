class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        
        for i in range(len(items)):
            
            if ruleKey == 'type':
                
                if ruleValue == items[i][0]:
                    count += 1
                    
            elif ruleKey == 'color':
                
                if ruleValue == items[i][1]:
                    count += 1
                    
            else:
                
                if ruleValue == items[i][2]:
                    count += 1
                    
        return count