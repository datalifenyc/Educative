from undirect_graph import Graph
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


def is_tree(g):
    for i in range(g.vertices):
        if g.array[i].head_node == None:
            return False


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.print_graph()


a = Graph(5)
a.add_edge(0, 1)
a.add_edge(0, 2)
a.add_edge(2, 3)
a.add_edge(3, 4)
a.add_edge(0, 4)
a.print_graph()
