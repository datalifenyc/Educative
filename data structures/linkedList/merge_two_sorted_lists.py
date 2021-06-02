from LinkedList import LinkedList


def mergeTwoLists(l1, l2):
    l3 = LinkedList()
    temp = LinkedList()
    while l1 and l2:
        if l1.head_node.data <= l2.head_node.data:
            l3 = l1
            l1 = l1.next
            temp.next = l1
        else:
            l3 = l2
            l2 = l2.next
            temp.next = l2
        temp = l3
        l3 = l3.next
    while l1:
        l3 = l1
        l1 = l1.next
        l3 = l3.next
    while l2:
        l3 = l2
        l2 = l2.next
        l3 = l3.next
    return l3


l1 = LinkedList()
l1.insert_at_head(1)
l1.insert_at_tail(2)
l1.insert_at_tail(4)


l2 = LinkedList()
l2.insert_at_head(1)
l2.insert_at_tail(3)
l2.insert_at_tail(4)

mergeTwoLists(l1, l2)
