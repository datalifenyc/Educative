from Graph import Graph
from Queue import MyQueue
from Stack import MyStack
# You can check the input graph in console tab

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# class Graph => {int vertices, linkedList[] array}
# class linkedList => {Node head_node}
# class Node => {int data, Node next_element}


def detect_cycle(g):
    # Write your code here
    result = ""
    source = 0
    d = {}
    q = MyQueue()
    num_of_vertices = g.vertices
    for num in range(num_of_vertices):
        d[num] = 0
    q.enqueue(source)
    while not q.is_empty():
        out = q.dequeue()
        current_node = g.array[out].get_head()
        d[out] = d[out] + 1
        while current_node:
            q.enqueue(current_node.data)
            current_node = current_node.next_element
        if d[out] > 1:
            return True
        # Write - Your - Code
        # For the above graph, it should return "01234" or "02143" etc
    return False

# Create any helper functions here


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.print_graph()
print(detect_cycle(g))
