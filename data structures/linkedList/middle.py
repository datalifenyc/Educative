from LinkedList import LinkedList
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Length of the list => list.length()
# Node class  { int data ; Node next_element;}


def find_mid(lst):
    middle = 0
    if lst.length() % 2 == 1:
        middle = lst.length()//2 + 1
    else:
        middle = lst.length()//2

    i = 1
    current_node = lst.get_head()
    while current_node:
        if i == middle:
            return current_node.data
        current_node = current_node.next_element
        i += 1


lst = LinkedList()
lst.insert_at_head(4)
lst.insert_at_head(3)
lst.insert_at_head(2)
lst.insert_at_head(1)
lst.insert_at_head(0)
print(find_mid(lst))
