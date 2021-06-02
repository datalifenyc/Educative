from Node import Node
from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def reverse(lst):
    currentNode = lst.get_head()
    new_list = LinkedList()
    while currentNode is not None:
        new_list.insert_at_head(currentNode.data)
        currentNode = currentNode.next_element
    lst.head_node = new_list.get_head()

    return lst


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
lst.insert_at_head(0)
lst.print_list()
reverse(lst)
lst.print_list()
