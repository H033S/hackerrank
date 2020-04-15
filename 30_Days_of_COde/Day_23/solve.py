import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        q = [root]
        ans = []

        while q:
            u = q.pop(0)

            ans.append(u.data)
            
            if u.left:
                q.append(u.left)
            if u.right:
                q.append(u.right)
        
        for x in ans:
            print(x, end=" ")

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
