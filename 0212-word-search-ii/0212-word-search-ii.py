class TireNode:
    def __init__(self):
        self.isend = False
        self.node = None
        self.children = {}
class Tire:
    def __init__(self):
        self.root = TireNode()
    def insert(self , word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TireNode()
            node = node.children[ch]
        node.isend = True
        node.word = word
         
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m , n = len(board) , len(board[0])
        trie = Tire()
        for word in words:
            trie.insert(word)
        visited = [[False] * n for _ in range(m)]
        rst = []

        def dfs(i , j ,parent):
            if not(0<= i < m and 0 <= j < n and not visited[i][j]):
                return  
            c = board[i][j]
            if not c in parent.children:
                return
            node = parent.children[c]
            visited[i][j] = True
            if node.isend and node.word:
                word = node.word
                rst.append(word)
                node.word = None
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                dfs(i + dx, j + dy, node)

            visited[i][j] = False
            if not node.children and node.isend == False:
                del parent.children[c]


    
        for i in range(m):
            for j in range(n):
                dfs(i , j , trie.root)
        
        return rst


        