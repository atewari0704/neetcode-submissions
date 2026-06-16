class Solution:
    def simplifyPath(self, path: str) -> str:
        reconstruct = []
        for word in path.split("/"):
            if word:
                reconstruct.append(word)
        
        stack = []

        for word in reconstruct:
            if word == ".":
                continue
            if word == "..":
                if stack:
                    stack.pop()
            else:
                stack.append("/" + word)
        
        return "".join(stack) if stack else "/"


        