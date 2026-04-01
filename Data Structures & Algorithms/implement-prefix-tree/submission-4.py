class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        curr = self.root

        # For every character, if it doesn't exist yet, 
        # create a new TrieNode and link in the hashmap
        # Set the last character to true end
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        # For every character, keep traversing until
        # end of word is reached, otherwise return False
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        # For every character, traverse until prefix
        # is complete. If unable to complete, return False
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
        