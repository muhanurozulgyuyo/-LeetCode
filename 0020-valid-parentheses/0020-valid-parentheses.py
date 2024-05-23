class Solution:
    def isValid(self, s: str) -> bool:
        S = Stack()
        for i in s:
            if i in '({[':
                S.push(i)
            else:
                if i == ')':
                    if S.peek() == '(':
                        S.pop()
                    else:
                        return False
                elif i == '}':
                    if S.peek() == '{':
                        S.pop()
                    else:
                        return False
                elif i == ']':
                    if S.peek() == '[':
                        S.pop()
                    else:
                        return False
        return S.is_empty()
class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            self.items.pop()
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         bracket_map = {')': '(', '}': '{', ']': '['}

#         for char in s:
#             if char in bracket_map.values():  # 여는 괄호일 경우
#                 stack.append(char)
#             elif char in bracket_map.keys():  # 닫는 괄호일 경우
#                 if stack == [] or stack[-1] != bracket_map[char]:
#                     return False
#                 stack.pop()
#             else:
#                 return False  # 유효하지 않은 문자(괄호가 아님)

#         return stack == []
