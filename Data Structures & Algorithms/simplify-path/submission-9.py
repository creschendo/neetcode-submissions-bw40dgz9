class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        curr = ""

        # use slashes as separators, add a slash so last "word" is processed
        for char in path + "/":
            if char == "/":

                # if current word is double dot, pop 
                # last directory if possible
                if curr == "..":
                    if stack:
                        stack.pop()

                # if no double dot, and valid directory, append
                elif curr != "" and curr != ".":
                    stack.append(curr)

                # reset current word
                curr = ""

            # middle of a word, just add next character
            else:
                curr += char

        # add a starting slash
        return "/" + "/".join(stack)