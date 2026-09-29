'''
Operations on Singly Linked List

1. Insertion:
    a. At the beginning
    b. At the end
    c. At a given position
2. Deletion:
    a. At the beginning
    b. At the end
    c. At a given position
3. Traversal
4. Updation

from platform import node


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_beginning(head, data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return head
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, data, position):
    if head is None:
        print("Error: The linked list is empty.")
        return
    new_node = Node(data)
    new_node.next = node.next
    node.next = new_node 

def traverse(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
head = None

head = insert_at_beginning(head, 10)
head = insert_at_beginning(head, 20)
head = insert_at_beginning(head, 30)
print("Linked List after insertion at the beginning:")
traverse(head)

print("\nLinked List after insertion at the end:")
insert_at_end(head, 40)
traverse(head)
print()

print("Linked List after insertion at a given position:")
insert_at_position(head, 25, 2)
traverse(head)
print()
'''