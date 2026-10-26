class TrieNode: # stores the character and the neighbors.
    def __init__(self, val: str=None):
        self.val = val
        self.neighbors = [None] * 26 
        self.is_end = False

class PrefixTree:
        
    def __init__(self):
        self.root = TrieNode() # root node always starts out with a null reference. All starting characters of each word in the trie are NEIGHBORS of the root node (node with null ref).

    def insert(self, word: str) -> None:
        t_node = self.root # traversal node
        for c in word:
            """
            FIX: check if the neighbor we're looking for is null. If NOT null, then DO NOT create a new TrieNode. Otherwise, do so. 
            """
            if not t_node.neighbors[ord(c) - ord('a')]:
                t_node.neighbors[ord(c) - ord('a')] = TrieNode(c) 
            t_node = t_node.neighbors[ord(c) - ord('a')]
        # when we reach the end of the string, mark the last character as the end of the node.
        t_node.is_end = True

    def search(self, word: str) -> bool:
        t_node = self.root # traversal is similar to a linked list
        for c in word:
            t_node = t_node.neighbors[ord(c) - ord('a')]
            # if at any point t_node becomes null, we know "word" is not in the list
            if not t_node:
                return False
        
        return t_node.is_end

    def startsWith(self, prefix: str) -> bool:
        t_node = self.root
        for c in prefix:
            t_node = t_node.neighbors[ord(c) - ord('a')]
            if not t_node:
                return False
        # checking if the node we end at has ANY neighbors. This means we've inserted a word with the prefix "prefix"
        return t_node != None
        