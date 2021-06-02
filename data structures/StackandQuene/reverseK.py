from Queue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if k < 0 or queue.size() < k:
        return None
    lst = [0]*k
    lst2 = [0]*(queue.size() - k)

    for i in range(k):
        lst[i] = queue.dequeue()

    for i in range(len(lst)):
        queue.enqueue(lst.pop())
    for i in range(queue.size() - k):
        queue.enqueue(queue.dequeue())

    return queue.queue_list


q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.enqueue(10)

print(reverseK(q, 11))
