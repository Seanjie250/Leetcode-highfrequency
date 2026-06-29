class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = None
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m , n = len(board) , len(board[0])
        root = TrieNode()
        for word in words:
            node = root
            for cr in word:
                if cr not in node.children:
                    node.children[cr] = TrieNode()
                node = node.children[cr]
            node.end = word

        print(root)
        rst = []
        def dfs(node, i , j):
            char = board[i][j]
            if char not in node.children:
                return
            cur_node = node.children[char]
            if cur_node.end:
                rst.append(cur_node.end)
                cur_node.end = None
            board[i][j] = '#'
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = i + dr, j + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] != "#":
                    dfs(cur_node , nr, nc)
            board[i][j] = char

        for i in range(m):
            for j in range(n):
                dfs(root , i , j)
        return rst

            
            

        