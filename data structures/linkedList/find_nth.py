from LinkedList import LinkedList


def find_nth(lst, n):
    # Write your code here
    if lst.length() < n:
        return -1
    complement_n = lst.length() - n
    current_node = lst.get_head()
    for i in range(complement_n):
        current_node = current_node.next_element

    return current_node.data


list1 = LinkedList()
list1.insert_at_head(99)
list1.insert_at_head(39)
list1.insert_at_head(47)
list1.insert_at_head(78)
list1.insert_at_head(60)
list1.insert_at_head(18)
list1.insert_at_head(22)
list1.print_list()

print(find_nth(list1, 7))
