class Node:
    def __init__(self,val,left,right):
        self.url = val
        self.left = left
        self.right = right

class BrowserHistory:
    def __init__(self, homepage: str):
        self.homepage = Node(homepage, None, None)
        self.cur = self.homepage

    def visit(self, url: str) -> None:
        self.cur.right = Node(url,self.cur,None)
        self.cur = self.cur.right
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.left:
            self.cur = self.cur.left
            steps -= 1
        
        return self.cur.url 

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.right:
            self.cur = self.cur.right
            steps -= 1

        return self.cur.url
       


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)