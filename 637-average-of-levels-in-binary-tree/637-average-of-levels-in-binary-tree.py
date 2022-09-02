# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        temp = []
        q=deque([None,root])
        while True:
            n=q.pop()
            if n:
                temp.append(n.val)
                if n.left:
                    q.appendleft(n.left)
                if n.right:
                    q.appendleft(n.right)
            else:
                ans.append(temp)
                temp = []
                if q:
                    q.appendleft(None)   
                else:
                    break
        res = []
        # print(ans)
        for i in range(len(ans)):
            s = 0
            # print(ans[i])
            for j in ans[i]:
                s += j
            ans[i] = s/len(ans[i])
        return ans
            
        