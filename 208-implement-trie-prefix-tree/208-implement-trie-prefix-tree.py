class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                curr_node.children[letter] = TrieNode()
            curr_node = curr_node.children[letter]
        curr_node.isEnd = True


    def search(self, word: str) -> bool:
        curr_node = self.root
        for letter in word:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return curr_node.isEnd


    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for letter in prefix:
            if letter not in curr_node.children:
                return False
            curr_node = curr_node.children[letter]
        return True