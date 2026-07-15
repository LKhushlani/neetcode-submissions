class Solution:
    def isValid(self, s: str) -> bool:

        b = { ")": "(", "]": "[", "}": "{"}

        stack = []
        # {}({})
        # stack = [ { ]

        for c in s:
            print("c", c)
            print(stack)
            if c in b.keys() and stack and stack[-1] == b[c]:
                print("stack", stack)
                stack.pop()
            else:

                stack.append(c)
                print("s", stack)

        return True if not stack else False


        