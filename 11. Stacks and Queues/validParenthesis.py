def isValid(self, s: str) -> bool:
        d  = {
            
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        
        stack = []
        
        for char in s:
            if(char in d):
                stack.append(char)
            
            elif stack:
                if char == d[stack[-1]]:
                    stack.pop()
                else:
                    return False
                
            else:
                return False
                
        return len(stack) == 0
            