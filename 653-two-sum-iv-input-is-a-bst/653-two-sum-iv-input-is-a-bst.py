# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def dll(root):
    if not root:
        return None,None
    lh, lt = dll(root.left)
    rh, rt = dll(root.right)
    if lh:
        l = lh
        lt.right = root
        root.left = lt
    else:
        l = root
    if rh:
        r = rt
        root.right = rh
        rh.left = root
    else:
        r = root
    return l,r

class Solution:
    
    
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l,r = dll(root)
        
        while l.val != r.val:
            sum = l.val + r.val
            if sum > k:
                r = r.left
            elif sum < k:
                l = l.right
            else:
                return True
        return False