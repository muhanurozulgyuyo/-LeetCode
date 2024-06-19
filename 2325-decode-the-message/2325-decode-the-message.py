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

# class Solution:
#     def decodeMessage(self, key: str, message: str) -> str:
#         # 1. 키의 첫 번째 등장 순서 추출
#         seen = set()
#         substitution_table = {}
#         alphabet = 'abcdefghijklmnopqrstuvwxyz'
#         index = 0
        
#         for char in key:
#             if char not in seen and char != ' ':
#                 seen.add(char)
#                 substitution_table[char] = alphabet[index]
#                 index += 1
        
#         # 2. 메시지 복호화
#         decoded_message = []
        
#         for char in message:
#             if char == ' ':
#                 decoded_message.append(' ')
#             else:
#                 decoded_message.append(substitution_table[char])
        
#         return ''.join(decoded_message)
           