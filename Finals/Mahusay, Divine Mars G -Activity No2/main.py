#Mahusay, Divine Mars G
#DSALGO1
#11/22/2024
#Activity 2 Finals
from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from LinkedDeque import LinkedDeque as Deque

Q = Queue()
D = Deque()
S = Stack()

# Initialize the deque with the starting elements
D.insert_first(8)
D.insert_first(7)
D.insert_first(6)
D.insert_first(5)
D.insert_first(4)
D.insert_first(3)
D.insert_first(2)
D.insert_first(1)

print("Queue Starting elements:")
print("D = ", D)
print("Queue =", Q)

Q.enqueue(D.delete_last())

Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())

Q.enqueue(D.delete_last())

D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())

D.insert_last(Q.dequeue())

Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())
Q.enqueue(D.delete_first())

D.insert_first(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())
D.insert_last(Q.dequeue())

Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
Q.enqueue(D.delete_last())
D.insert_first(Q.dequeue())
D.insert_first(Q.dequeue())
D.insert_first(Q.dequeue())

print("Queue Final state:")
print("D =", D)
print("Queue =", Q)

D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.delete_first()
D.insert_first(8)
D.insert_first(7)
D.insert_first(6)
D.insert_first(5)
D.insert_first(4)
D.insert_first(3)
D.insert_first(2)
D.insert_first(1)

print("")

print("Stack Starting elements: ")
print("D =",D)
print("Stack = ", S)

S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())

D.insert_first(D.delete_last())
D.insert_first(D.delete_last())
S.push(D.delete_first())
S.push(D.delete_first())

D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())

S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())
S.push(D.delete_last())

D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())
D.insert_last(S.pop())



print("Stack Final state:")
print("D =", D)
print("Stack =", S)