#queue
#insertion enqueue
#deletion dequeue
#first in first out fifo

que=[]
size=int(input("Enter size"))
front=0
rear=0
n=0

def insert():
    global front,rear,size,que
    if(rear>=size):
        print("Queue is full")
    else:
        p=int(input("Enter element want to insert"))
        que.insert(rear,p)
        #insert(position,element)
        rear+=1

        for i in range(front,rear):
            print(que[i])

def delete():
    global front,rear,size,que
    if(rear==front):
        print("Queue is empty")
    else:
        front+=1
        for i in range(front,rear):
            print(que[i])


while(n!=1):
    print("Enter the operation want to perform")
    opt=int(input("press \n1)Enqueue \n2)Dequeue\n "))
    if(opt==1):
        insert()
    elif opt==2:
        delete()

    n=int(input("Do you want to continue press 1 for exit"))
