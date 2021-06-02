from Graph import Graph
from Queue import MyQueue
# You can check the input graph in console tab

# Create Queue => queue = MyQueue()
# Functions of Queue => enqueue(int), dequeue(), size(), front(), is_empty()
# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty()
# Create Graph => graph = Graph(vertices)
# Create LinkedList => link_list = LinkedList()
# Functions of LinkedList => insert_at_head(Node), is_empty(), delete(),
#                            delete_at_head(list), search(), print_list()
# class Node => data, next_element
# Breadth First Traversal of Graph g from source vertex


def bfs_traversal(g, source):
    result = ""
    q = MyQueue()
    num_of_vertices = g.vertices
    q.enqueue(source)
    while not q.is_empty():
        out = q.dequeue()
        current_node = g.array[out].get_head()
        while current_node:
            q.enqueue(current_node.data)
            current_node = current_node.next_element
        result = result + str(out)
        # Write - Your - Code
        # For the above graph, it should return "01234" or "02143" etc
    return result


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.print_graph()
print(bfs_traversal(g, 0))
