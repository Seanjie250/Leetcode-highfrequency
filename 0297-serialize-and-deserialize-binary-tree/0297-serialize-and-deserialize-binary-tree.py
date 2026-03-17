# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        rst = []
        def helper(node):
            if not node:
                rst.append('null')
                return
            rst.append(str(node.val))
            helper(node.left)
            helper(node.right)
        helper(root)
        print(rst)
        return ','.join(rst)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        datalist = data.split(',')
        q = deque(datalist)
        def helper():
            if not q:
                return None
            first_node = q.popleft()
            if first_node == 'null':
                return None
            root = TreeNode(int(first_node))
            root.left = helper()
            root.right = helper()
            return root
        root = helper()
        return root


            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))