# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        rst = []
        def dfs(node):
            if not node:
                rst.append('None')
            else:
                rst.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return ','.join(rst)

        

    def deserialize(self, data):
        val = data.split(',')
        print(val)
        def dfs():
            if val[0] == 'None':
                val.pop(0)
                return None
            else:
                node = TreeNode(int(val.pop(0)))
                node.left = dfs()
                node.right = dfs()
            return node
        root = dfs()
        return root

                
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))