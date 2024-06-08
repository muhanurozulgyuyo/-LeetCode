class Solution:
    def fib(self, n: int) -> int:
        # 기본 경우: F(0) = 0, F(1) = 1
        if n == 0:
            return 0
        elif n == 1:
            return 1
        
        # F(2)부터는 이전 두 값을 더해서 계산
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        
        return b
