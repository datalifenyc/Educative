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


def num_edges(g):
    result = 0
    for i in range(g.vertices):
        temp = g.array[i].head_node
        while temp:
            if temp.data < i:
                result = result + 1
            temp = temp.next_element
        # Write - Your - Code
        # For the above graph, it should return "01234" or "02143" etc
    return result


g = Graph(7)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
g.print_graph()
print(num_edges(g))
