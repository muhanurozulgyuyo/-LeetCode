# TreeNode 클래스 정의
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 클래스 정의
class Solution:
    def evaluateTree(self, root: TreeNode) -> bool:
        # 리프 노드일 경우, 해당 값 반환
        if root.left is None and root.right is None:
            return root.val == 1
        
        # 왼쪽 자식과 오른쪽 자식을 재귀적으로 평가
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # 비 리프 노드일 경우, 논리 연산 수행
        if root.val == 2:  # OR 연산
            return left_val or right_val
        elif root.val == 3:  # AND 연산
            return left_val and right_val
