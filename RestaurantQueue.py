from collections import deque
import time
import threading

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
    
myQueue=Queue()
def placeOrders(orders):
    for order in orders:
        print ('Placing order for: {}'.format(order))
        myQueue.enqueue(order)
        time.sleep(0.5)
        
        
def serveOrders():
    while True:
        if not myQueue.is_empty():
            print('Now serving: {}'.format(myQueue.dequeue()))
            time.sleep(2)
        else:
            print('There are no more orders left')
            break

def main():
    order=['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=placeOrders,args=(order,))
    t2=threading.Thread(target=serveOrders)

    t1.start()
    time.sleep(1)
    t2.start()
    
if __name__=='__main__':    
    main()


