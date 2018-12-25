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
    
    numCl = False
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(i)
            opening_brackets_stack.append(next)
            
        if next == ')' or next == ']' or next == '}':
            numCl = True
            brc = opening_brackets_stack.pop()
            n = opening_brackets_stack.pop()
            B = Bracket(brc,n)
            
            if B.Match(next):
            	pass
            if not B.Match(next):
            	print(i+1)
            	exit()
    if not numCl:
    	print(len(text))
    	exit()
     
    print("Success")      	
                
    




    # Printing answer, write your code here
