class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [''] * len(s)
        for i in range(len(s)):
            answer[indices[i]] = s[i]
        # for idx, char in zip(indices, s):
        #     answer[idx] = char
        return ''.join(answer)
            