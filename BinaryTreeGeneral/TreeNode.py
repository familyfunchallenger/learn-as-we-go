# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def generateTreeFromBFS(arr):
        if len(arr) == 0:
            return None
        head = TreeNode(arr[0])
        if len(arr) == 1:
            return head
        nodes = {}
        nodes[0] = head
        i = 0
        while i < len(arr):
            l = 2 * i + 1
            if l < len(arr):
                n = TreeNode(arr[l])
                nodes[i].left = n
                nodes[l] = n
            if l + 1 < len(arr):
                n = TreeNode(arr[l + 1])
                nodes[i].right = n
                nodes[l + 1] = n
            i += 1
        return head
    
    @staticmethod
    def printTreeBFS(head):
        if head is None:
            print([])
            return
        p = head
        nodes = [p]
        bfs = []
        while len(nodes) > 0:
            if nodes[0] is not None:
                bfs.append(nodes[0].val)
                nodes.append(nodes[0].left)
                nodes.append(nodes[0].right)
            else:
                bfs.append(None)
            nodes.remove(nodes[0])
        while len(bfs) > 0 and bfs[-1] is None:
            bfs.pop()
        print(bfs)



#arr = [3, 9, 20, None, None, 15, 7]
#t = TreeNode.generateTreeFromBFS(arr)
#TreeNode.printTreeBFS(t)
