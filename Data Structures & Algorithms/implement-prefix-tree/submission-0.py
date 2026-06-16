class Node:
    def __init__(self,letter):
        self.letter = letter
        self.end = False #default is False
        self.children = dict()


class PrefixTree:
    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
        cur = self.root

        for letter in word:
            if letter in cur.children:
                cur = cur.children[letter]
                continue
            
            else:
                ahead = Node(letter)
                cur.children[letter] = ahead
                cur = ahead
        
        cur.end = True # marks the end of the word when we make the node for the last letter

    def search(self, word: str) -> bool:
        cur = self.root

        for letter in word:
            if letter not in cur.children:
                return False
            
            else:
                cur = cur.children[letter]

        return cur.end
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for letter in prefix:
            if letter not in cur.children:
                return False
            
            else:
                cur = cur.children[letter]
                
        return True
        
        
        