class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        list_str = '['
        while current is not None:
            list_str += str(current.data) + ', '
            current = current.next
        return list_str.removesuffix(', ') + ']'

    def __repr__(self):
        return str(self)

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(value)

    def show_elements(self):
        print(str(self))

    def length(self):
        result = 0
        current = self.head
        while current is not None:
            result += 1
            current = current.next
        return result

    def get_element(self, position):
        i = 0
        current = self.head
        while current is not None:
            if i == position:
                return current.data
            current = current.next
            i += 1
        return None


def reverse(ll):
    if ll.head is None:
        return

    current_node = ll.head
    prev_node = None

    while current_node is not None:
        # Track the next node
        next_node = current_node.next

        # Modify the current node
        current_node.next = prev_node

        # Update prev and current
        prev_node = current_node
        current_node = next_node

    ll.head = prev_node


if __name__ == '__main__':
    list1 = LinkedList()
    list1.append(2)
    list1.append(3)
    list1.append(5)
    list1.append(9)
    print(list1)
    reverse(list1)
    list1.show_elements()
