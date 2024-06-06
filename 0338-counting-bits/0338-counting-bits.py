class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        # 1부터 n까지 반복하여 각 숫자의 1의 개수를 계산합니다.
        for i in range(1, n + 1):
            # 점화식을 사용하여 1의 개수를 계산합니다.
            ans[i] = ans[i >> 1] + (i & 1)

        return ans