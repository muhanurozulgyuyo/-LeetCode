# 트리 노드를 정의하는 클래스
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 트리가 비어있다면 그대로 반환
        if root is None:
            return None
        
        # 현재 노드의 왼쪽과 오른쪽 자식을 교환
        root.left, root.right = root.right, root.left
        
        # 왼쪽 자식 노드를 재귀적으로 뒤집기
        self.invertTree(root.left)
        
        # 오른쪽 자식 노드를 재귀적으로 뒤집기
        self.invertTree(root.right)
        
        # 루트를 반환
        return root
