class TireNode:
    def __init__(self):
        self.children = {}
        self.isend = False
class Trie:
    def __init__(self):
        self.root = TireNode()
    def insert(self , word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TireNode()
            node = node.children[ch]
        self.isend = True
        

    def search(self , word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        return self.isend
        

    def startsWith(self , prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            else:
                node = node.children[ch]
        return True
        

