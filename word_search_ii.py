class Node:
    def __init__(self, c):
        self.char = c
        self.children = {}
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.prevInsert = None

    def insert(self, word: str) -> None:
        self.insertRec(self.root, word)
        self.prevInsert = word

    def insertRec(self, root, word):
        if root is None or len(word) == 0:
            return

        if word[0] in root.children:
            if len(word) == 1:
                root.children[word[0]].wordEnd = True
            self.insertRec(root.children[word[0]], word[1:])
        else:
            node = Node(word[0])
            if len(word) == 1:
                node.wordEnd = True
            root.children[word[0]] = node
            self.insertRec(node, word[1:])
        

    def search(self, word: str) -> bool:
        return self.searchRec(self.root, word)

    def searchRec(self, root, word):
        if word[0] in root.children:
            if len(word) == 1:
                return root.children[word[0]].wordEnd
            return self.searchRec(root.children[word[0]], word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithRec(self.root, prefix)

    def startsWithRec(self, root, prefix):
        if root is None:
            return False
        if len(prefix) == 0:
            return True
        if prefix[0] in root.children:
            return self.startsWithRec(root.children[prefix[0]], prefix[1:])
        else:
            return False

class Solution:
    def findWords(self, board, words):
        # Create a trie with all of the words inserted
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        # Set of tuples represented the (r, c) index of the board
        found = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.boardDfs(board, (r, c), found, self.trie.root, "")
        return list(found)
        
    def boardDfs(self, board, position, found, root, string):
        r, c = position 
        if board[r][c] == "@":
            return
        if root is None:
            return
        char = board[r][c]
        board[r][c] = "@"
        if char in root.children:
            if root.children[char].wordEnd:
                found.add(string + char)
                root.children[char].found = False
            if r - 1 >= 0:
                self.boardDfs(board, (r - 1, c), found, root.children[char], string + char)
            if r + 1 < len(board):
                self.boardDfs(board, (r + 1, c), found, root.children[char], string + char)
            if c - 1 >= 0:
                self.boardDfs(board, (r, c - 1), found, root.children[char], string + char)
            if c + 1 < len(board[0]):
                self.boardDfs(board, (r, c + 1), found, root.children[char], string + char)
        board[r][c] = char


