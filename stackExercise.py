from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self,val):
        self.container.append(val)
        
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return  self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    def reverse_string(self,s):
        return s[::-1]
    
if __name__ =='__main__':
    ourStack=Stack()
    print(ourStack.reverse_string('We will conquere COVID-19'))