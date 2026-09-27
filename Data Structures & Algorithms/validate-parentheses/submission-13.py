class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        #Starts off with a closing bracket   
        if s[0]==")" or s [0] =="}" or s[0]=="]":
            return False

        for c in s:

            if c == "{" or c=="[" or c=="(":
                stack.append(c)
            
            elif (stack and ((c=="}" and stack[-1]=="{") or (c==")" and stack[-1]=="(") or (c=="]" and stack[-1]=="["))):
                stack.pop()
            else :
                return False

        if stack:
            return False
        else:
            return True
