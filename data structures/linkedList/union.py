from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    storage = {}
    list1_current_node = list1.get_head()
    while list1_current_node:
        storage[list1_current_node.data] = 1
        list1_current_node = list1_current_node.next_element

    list2_current_node = list2.get_head()
    while list2_current_node:
        if list2_current_node.data not in storage:
            list1.insert_at_tail(list2_current_node.data)
        list2_current_node = list2_current_node.next_element

    return list1


list1 = LinkedList()
list1.insert_at_head(60)
list1.insert_at_head(80)
list1.insert_at_head(20)
list1.insert_at_head(10)
list1.print_list()

list2 = LinkedList()
list2.insert_at_head(45)
list2.insert_at_head(60)
list2.insert_at_head(30)
list2.insert_at_head(20)
list2.insert_at_head(15)
list2.print_list()

union(list1, list2)
list1.print_list()
