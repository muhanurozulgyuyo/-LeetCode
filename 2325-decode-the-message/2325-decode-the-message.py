

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # 1. 키의 첫 번째 등장 순서 추출
        seen = set()
        substitution_table = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        index = 0
        
        for char in key:
            if char not in seen and char != ' ':
                seen.add(char)
                substitution_table[char] = alphabet[index]
                index += 1
        
        # 2. 메시지 복호화
        decoded_message = []
        
        for char in message:
            if char == ' ':
                decoded_message.append(' ')
            else:
                decoded_message.append(substitution_table[char])
        
        return ''.join(decoded_message)
           