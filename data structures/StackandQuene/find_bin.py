from Queue import MyQueue


def find_bin(number):
    q = MyQueue()
    for i in range(1, number+1):
        bin = "{0:b}".format(i)
        q.enqueue(bin)
    return q.queue_list


n = 3
print(find_bin(n))
