# find_mother_vertex_ce.py

"""
educative.io

Data Structures for Coding Interviews in Python
https://www.educative.io/courses/data-structures-coding-interviews-python

Challenge 4: Find a "Mother Vertex" in a Directed Graph
https://www.educative.io/courses/data-structures-coding-interviews-python/7nODy1vm2vj

Notes:
Review solution
"""

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
#hello
def find_mother_vertex(g):
    # Write - Your - Code
    '''
    Returns value of mother vertex. If none, returns -1.

    Constraints
    -----------
    Return only one mother vertex.

    Input
    -----
    g : Graph()
        directed graph

    Output
    ------
    mother_vertex : int
        value of mother_vertex
    '''
    current_mother_vertex = None
    current_total = 0
    for i in range(g.vertices):
        total_connected_vertices = dfs_traversal(g, i)
        if total_connected_vertices > current_total:
            current_total = total_connected_vertices
            current_mother_vertex = i
    if current_total == 0:
        return -1
    else:
        return current_mother_vertex

# Create helper functions here
def dfs_traversal(g, source):
    '''
    Return the number of connected vertices
    for each node.

    Constraints
    -----------

    Input
    -----
    g : Graph
        directed graph

    source : int
        starting vertices of graph

    Output
    ------
    connected_vertices : int
        Number of connected vertices for each
        vertex
    '''
    # Count the number of vertices
    vertices_count = g.vertices
    # Create variable for number of vertices
    # that have been reached
    num_of_vertices_visited = 0
    # Create a list to track whether a vertex
    # has been visited.
    vertices_tracker = [False] * vertices_count
    # Create a stack to store the visited sources
    s = MyStack()
    # Push the current source on to the stack
    s.push(source)
    # Set the vertices_tracker to True at the 
    # index representing the current source
    vertices_tracker[source] = True
    # Loop through the stack until every connected
    # vertex is reached
    while s.is_empty() == False:
        # Pop a vertex from the stack
        current_vertex = s.pop()
        # Store value of current vertex
        vertex = g.array[current_vertex].head_node
        # Check whether vertex has been visited
        while vertex is not None:
            # check if visited is false
            if vertices_tracker[vertex.data] == False:
                # Push to stack if not visited
                s.push(vertex.data)
                vertices_tracker[vertex.data] = True
                num_of_vertices_visited += 1
            vertex = vertex.next_element
    # Return a count of the number of vertices
    # visited
    return num_of_vertices_visited + 1

if __name__ == '__main__':
    '''   
    g = Graph(4)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.print_graph()
    '''
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    # g.add_edge(1, 3)
    g.add_edge(2, 4)
    print(find_mother_vertex(g))

