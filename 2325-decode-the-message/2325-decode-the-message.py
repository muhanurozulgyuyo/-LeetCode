import string

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        converter = {}
        alphabet = string.ascii_lowercase
        answer = []
        
        key = key.replace(' ', '')
        
        key_cnt = 0
        alp_cnt = 0
        
        while alp_cnt < len(alphabet):
            
            if key[key_cnt] not in converter.keys():
                converter[key[key_cnt]] = alphabet[alp_cnt]
                key_cnt += 1
                alp_cnt += 1
            else:
                key_cnt += 1
            
        for s in message:
            
            if s == ' ':
                answer.append(' ')
            else:
                answer.append(converter[s])
                
        return ''.join(answer)
            