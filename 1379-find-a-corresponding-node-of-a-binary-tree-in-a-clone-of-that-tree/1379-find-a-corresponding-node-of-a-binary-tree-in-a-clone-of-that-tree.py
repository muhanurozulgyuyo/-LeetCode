# 이진 트리 노드에 대한 정의
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # 기본 경우: 원본 노드가 None이면 None을 반환
        if not original:
            return None
        
        # 현재 원본 트리의 노드가 타겟 노드라면
        if original == target:
            return cloned
        
        # 왼쪽 서브트리에 대해 재귀 호출
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result
        
        # 오른쪽 서브트리에 대해 재귀 호출
        return self.getTargetCopy(original.right, cloned.right, target)
