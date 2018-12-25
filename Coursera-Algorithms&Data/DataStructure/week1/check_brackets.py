# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    
    numOp = 0
    numCl = 0 
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            numOp += 1
            
            opening_brackets_stack.append(i)
            opening_brackets_stack.append(next)
            
        if next == ')' or next == ']' or next == '}':
            numCl += 1
            
            if len(opening_brackets_stack) == 0:
                print(i+1)
                exit()
            else:
                brc = opening_brackets_stack.pop()
                n = opening_brackets_stack.pop()
                B = Bracket(brc,n)
                
                if B.Match(next):
                    pass
                if not B.Match(next):
                    print(i+1)
                    exit()
    
    
    if numCl == 0:
        print(numOp) 
        exit()
    elif len(opening_brackets_stack) != 0:
        print(opening_brackets_stack[0]+1)
    else:
        print("Success")      	
                
    




    # Printing answer, write your code here
