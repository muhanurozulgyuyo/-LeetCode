# 트리 노드의 정의
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 루트가 None인 경우 깊이는 0
        if not root:
            return 0
        
        # 왼쪽 및 오른쪽 하위 트리의 깊이를 재귀적으로 계산
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # 현재 노드의 깊이는 왼쪽 및 오른쪽 하위 트리 깊이 중 더 큰 값에 1을 더한 값
        return max(left_depth, right_depth) + 1
