from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def remove_duplicates(lst):
    storage = {}
    current_node = lst.get_head()
    previous_node = None

    while current_node is not None:
        if current_node.data not in storage:
            storage[current_node.data] = True
        else:
            previous_node.next_element = current_node.next_element
            current_node.next_element = None
            current_node = previous_node.next_element
            continue
        previous_node = current_node
        current_node = current_node.next_element
    return lst


lst = LinkedList()
lst.insert_at_head(7)
lst.insert_at_head(22)
lst.insert_at_head(14)
lst.insert_at_head(21)
lst.insert_at_head(14)
lst.insert_at_head(7)
lst.print_list()
remove_duplicates(lst)
lst.print_list()
