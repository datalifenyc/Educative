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


def remove_edge(graph, source, dest):
    temp = graph.array[source].head_node
    previous_node = None
    if temp.data is dest:
        graph.array[source].delete_at_head()  # Use the previous function
        return graph

    while current_node is not None:
        # Node to delete is found
        if dest is current_node.data:
            # previous node now points to next node
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            break
        previous_node = current_node
        current_node = current_node.next_element
    return graph


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(4, 0)
g.print_graph()
print(remove_edge(g, 2, 3))
