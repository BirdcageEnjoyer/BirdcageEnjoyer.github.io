#example dequeue() procedure subroutine
size = 0
front = 0 #just sample variables to allow subroutine to be declared
max_size = 5

def dequeue():
    if size == 0:
        print("queue is empty")
    else:
        front += 1
        front = print(front % max_size)
        size -= 1