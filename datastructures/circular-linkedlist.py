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


def insert_after(prev_node, data):
    new_node = Node(data)
    new_node.next = prev_node.next
    prev_node.next = new_node


nodes = [Node(1), Node(19), Node(4), Node(5), Node(8)]
list = LinkedList()

for i in range(len(nodes)):
    if i < len(nodes) - 1:
        nodes[i].next = nodes[i+1]
    if i == 0:
        list.head = nodes[i]
    elif i == len(nodes) - 1:
        nodes[i].next = list.head
        list.tail = nodes[i]

def main():
    print("==Print nodes of circular linked list==")
    list.print_nodes()
    print("==Push node to the front==")
    list.push_front(100)
    list.print_nodes()
    print("==Insert node after specific node==")
    insert_after(list.head, 70)
    insert_after(list.tail, 777)
    list.print_nodes()
    print("==Append linked list to the back==")
    list.append(40000)
    list.print_nodes()
    print("==Delete node using value==")
    list.delete(4)
    list.delete(40000)
    list.delete(100)
    list.print_nodes()

if __name__ == "__main__":
    main()
