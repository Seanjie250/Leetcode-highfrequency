class TrieNode:
    def __init__(self):
        self.isend = False
        self.children = {}
class Trie:

    def __init__(self):
        self.root = TrieNode()
    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if not ch in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isend = True
    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if not ch in node.children:
                return False
            else:
                node = node.children[ch]
        return node.isend
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if not ch in node.children:
                return False
            else:
                node = node.children[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)