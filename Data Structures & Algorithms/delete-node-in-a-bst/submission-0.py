# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # node for deletion has no children
        # you would essentially replace the deleted node with either None or the value that would replace it

        # recursive

        # node for deletion has children

        # recursive solution
        # curnode.left or .right = recursive solution

        # if node for deletion is a match and no children then return None
        # if there are children then I replace the node for deltion with a child

        #htne delte the child

        # base case
        if not root: return None

        if key > root.val:
            root.right = self.deleteNode(root.right,key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)

        else:
            if not root.left and not root.right:
                return None

            if root.right:
                root.val = root.right.val
                root.right = self.deleteNode(root.right,root.right.val)
                return root
            
            else:
                root.val = root.left.val
                root.left = self.deleteNode(root.left,root.left.val)
                return root
        
        return root
            



        