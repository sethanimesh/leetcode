class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = [root]
        current_queue = []
        level = []
        result = []
        i = 1
        while queue!=[]:
            for root in queue:
                level.append(root.val)
                if root.left is not None:
                    current_queue.append(root.left)
                if root.right is not None:
                    current_queue.append(root.right)
            if i%2==0:
                result.append(level[::-1])
            else:
                result.append(level)
            i+=1
            level = []
            queue = current_queue
            current_queue = []
        return result
