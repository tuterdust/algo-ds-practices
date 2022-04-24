class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.tail.next = new_node

    def print_nodes(self):
        node = self.head
        while True:
            if node.next is self.head:
                print(node.data)
                break
            else:
                print(node.data, end=" ")
            node = node.next

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

    def delete(self, data):
        node = self.head
        prev_node = self.head
        while True:
            if node.data == data:
                if node is self.head:
                    self.tail.next = self.head.next
                    self.head = self.head.next
                elif node is self.tail:
                    prev_node.next = self.head
                    self.tail = prev_node
                    break
                else:
                    prev_node.next = node.next
            prev_node = node
            node = node.next
            if node.next is self.head and node.data != data:
                break


def sort_insert(linked_list, data):
    print(f"Inserting {data}")
    if linked_list.head is None:
        new_node = Node(data)
        new_node.next = new_node
        linked_list.head = new_node
        linked_list.tail = new_node
    elif data < linked_list.head.data:
        linked_list.push_front(data)
    else:
        node = linked_list.head
        while True:
            if node is linked_list.tail:
                linked_list.append(data)
                break
            if data >= node.data and data < node.next.data:
                new_node = Node(data)
                new_node.next = node.next
                node.next = new_node
                break

            node = node.next

def print_info(linked_list):
    linked_list.print_nodes()
    print(f"head is {linked_list.head.data}, tail is {linked_list.tail.data}",)

def main():
    test_list = LinkedList()
    sort_insert(test_list, 5)
    sort_insert(test_list, 4)
    sort_insert(test_list, 8)
    sort_insert(test_list, 7)
    sort_insert(test_list, 6)
    sort_insert(test_list, 2)
    print("==Print nodes of circular linked list==")
    print_info(test_list)
    print("==Push node to the front==")
    test_list.push_front(100)
    print_info(test_list)
    print("==Sort insert==")
    sort_insert(test_list, 101)
    sort_insert(test_list, 99)
    sort_insert(test_list, 101)
    sort_insert(test_list, 100)
    print_info(test_list)
    print("==Insert node after specific node==")
    print_info(test_list)
    print("==Append linked list to the back==")
    test_list.append(777)
    test_list.append(555)
    sort_insert(test_list, 576)
    print_info(test_list)
    print("==Delete node using value==")
    test_list.delete(576)
    test_list.delete(100)
    print_info(test_list)

if __name__ == "__main__":
    main()
