class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for letter in path + "/":
            if letter == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                        
                elif cur != "." and cur != "":
                    stack.append("/" + cur)

                cur = "" # reset the cur dir/file
            
            else:
                cur += letter
        
        return "".join(stack) if stack else "/"

































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


        