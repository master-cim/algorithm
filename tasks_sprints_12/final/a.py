MAX = 10


class Deque:
    def __init__(self, size):
        self.arr = [0] * MAX
        self.front = -1
        self.rear = 0
        self.size = size

    # Checks whether Deque is full or not.
    def isFull(self):
        return ((self.front == 0 and self.rear == self.size-1) or self.front == self.rear + 1)

    # Checks whether Deque is empty or not.
    def isEmpty (self):
        return (self.front == -1)

    # Inserts an element at front
    def insertfront(self, key):
        # check whether Deque if  full or not
        if (self.isFull()):
            print("Overflow")
            return
        # If queue is initially empty
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        # front is at first position of queue
        elif (self.front == 0):
            self.front = self.size - 1
        else: # decrement front end by '1'
            self.front = self.front-1
        # insert current element into Deque
        self.arr[self.front] = key

    # function to inset element at rear end
    # of Deque.
    def insertrear(self, key):
        if (self.isFull()):
            print(" Overflow")
            return
        # If queue is initially empty
        if (self.front == -1):
            self.front = 0
            self.rear = 0
        # rear is at last position of queue
        elif (self.rear == self.size-1):
            self.rear = 0
        # increment rear end by '1'
        else:
            self.rear = self.rear+1
        # insert current element into Deque
        self.arr[self.rear] = key

    # Deletes element at front end of Deque
    def deletefront(self):
        # check whether Deque is empty or not
        if (self.isEmpty()):
            print("Queue Underflow")
            return

        # Deque has only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        else:
            # back to initial position
            if (self.front == self.size - 1):
                self.front = 0
            else:  # increment front by '1' to remove current
                # front value from Deque
                self.front = self.front+1

    # Delete element at rear end of Deque
    def deleterear(self):
        if (self.isEmpty()):
            print(" Underflow")
            return

        # Deque has only one element
        if (self.front == self.rear):
            self.front = -1
            self.rear = -1
        elif (self.rear == 0):
            self.rear = self.size-1
        else:
            self.rear = self.rear-1

    # Returns front element of Deque
    def getFront(self):
        # check whether Deque is empty or not
        if (self.isEmpty()):
            print(" Underflow")
            return -1
        return self.arr[self.front]

    # function return rear element of Deque
    def getRear(self):
        # check whether Deque is empty or not
        if(self.isEmpty() or self.rear < 0):
            print(" Underflow")
            return -1
        return self.arr[self.rear]


def test():
    # Driver program to test above function
    dq = Deque(10)
    print("Insert element at rear end  : 5 ")
    dq.insertrear(5)
    print(dq.arr)
    print("insert element at rear end : 10 ")
    dq.insertrear(10)
    print(dq.arr)
    dq.insertrear(15)
    print(dq.arr)
    print("inserting element at front end")
    dq.insertfront(-5)
    print(dq.arr)
    dq.insertfront(-10)
    print(dq.arr)
    dq.insertfront(-15)
    print(dq.arr)
    print(f"get rear element : {dq.getRear()}")
    print(f"get front element: {dq.getFront()}")
    dq.deleterear()
    print(f"After delete rear element new rear become : {dq.getRear()}")
    print(dq.arr)
    dq.deletefront()
    print(f"After delete front element new front become : {dq.getFront()}")
    print(dq.arr)
    dq.insertrear(20)
    print(dq.arr)
    dq.insertfront(-20)
    print(dq.arr)
    dq.insertrear(25)
    print(dq.arr)
    dq.insertfront(-25)
    print(dq.arr)
    dq.insertrear(30)
    print(dq.arr)
    dq.insertfront(-30)
    print(dq.arr)
    dq.insertrear(1)
    print(dq.arr)
    dq.insertfront(-1)
    print(dq.arr)
    dq.deletefront()
    print(f"After delete front element new front become : {dq.getFront()}")
    print(dq.arr)



if __name__ == '__main__':
    test()
