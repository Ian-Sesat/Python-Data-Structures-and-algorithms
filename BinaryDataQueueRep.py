from collections import deque

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
    def front(self):
        return self.buffer[-1]

#Producing binary nunbers using a queueing function:
def produce_binary_numbers(n):
    myQueue=Queue()
    myQueue.enqueue('1')
    for i in range(n):
        q=myQueue.front()
        print(q)
        myQueue.enqueue(q+'0')
        myQueue.enqueue(q+'1')
        myQueue.dequeue()

def main():
    produce_binary_numbers(10)

if __name__=='__main__':    
    main()



