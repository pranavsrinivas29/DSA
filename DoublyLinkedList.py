class Node:
    def __init__(self, data):
        self.data = data  # Store the node's data
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head as None

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            new_node.next = self.head  # Link new node to the current head
            self.head.prev = new_node  # Link current head back to new node
            self.head = new_node  # Update head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if self.head is None:  # If the list is empty
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node  # Link the last node to the new node
            new_node.prev = current  # Link new node back to the last node

    def display_forward(self):
        current = self.head
        print("Forward traversal:")
        while current:
            prev_data = current.prev.data if current.prev else "None"
            next_data = current.next.data if current.next else "None"
            print(f"(Prev: {prev_data}) <- {current.data} -> (Next: {next_data})", end=" ")
            current = current.next
        print("")

    def display_backward(self):
        current = self.head
        if not current:
            print("The list is empty.")
            return

        # Go to the last node
        while current.next:
            current = current.next

        print("Backward traversal:")
        # Traverse backward
        while current:
            prev_data = current.prev.data if current.prev else "None"
            next_data = current.next.data if current.next else "None"
            print(f"(Prev: {prev_data}) <- {current.data} -> (Next: {next_data})", end=" ")
            current = current.prev
        print("")


# Example usage
dll = DoublyLinkedList()

# Insert elements at the beginning
dll.insert_at_beginning(10)
dll.insert_at_beginning(5)
print("List after inserting at the beginning:")
dll.display_forward()

# Insert elements at the end
dll.insert_at_end(20)
dll.insert_at_end(25)
print("List after inserting at the end:")
dll.display_forward()

print("List displayed backward:")
dll.display_backward()
