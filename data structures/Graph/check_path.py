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


def check_path(g, source, destination):
    q = MyQueue()
    q.enqueue(source)
    while not q.is_empty():
        out = q.dequeue()
        current_node = g.array[out].get_head()
        while current_node:
            q.enqueue(current_node.data)
            current_node = current_node.next_element
        if out == destination:
            return True
        # Write - Your - Code
        # For the above graph, it should return "01234" or "02143" etc
    return False


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.print_graph()
print(check_path(g, 1, 6))
