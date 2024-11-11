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
    
    def insert_at_position(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head
        current_position = 0

        while current is not None and current_position < position - 1:
            current = current.next
            current_position += 1

        if current is None:
            print("Position out of bounds.")
            return

        new_node.next = current.next
        new_node.prev = current

        if current.next:
            current.next.prev = new_node
        current.next = new_node
            
    def delete_at_beginning(self):
        if self.head is None:
            print("The list is empty. No nodes to delete.")
            return
        if self.head.next is None:  # Only one node in the list
            self.head = None
        else:
            self.head = self.head.next  # Move head to the next node
            self.head.prev = None       # Update the prev of new head to None

    def delete_at_end(self):
        if self.head is None:
            print("The list is empty. No nodes to delete.")
            return
        if self.head.next is None:  # Only one node in the list
            self.head = None
        else:
            current = self.head
            while current.next:  # Traverse to the last node
                current = current.next
            current.prev.next = None  # Unlink the last node

    def delete_at_position(self, position):
        if self.head is None:
            print("The list is empty. No nodes to delete.")
            return

        if position == 0:  # Delete the first node
            self.delete_at_beginning()
            return

        current = self.head
        current_position = 0

        # Traverse to the node at the specified position
        while current and current_position < position:
            current = current.next
            current_position += 1

        if current is None:
            print("Position out of bounds.")
            return

        # Delete the node at the specific position
        if current.next:  # If it's not the last node
            current.next.prev = current.prev
        if current.prev:  # If it's not the first node
            current.prev.next = current.next

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

# Delete at beginning
dll.delete_at_beginning()
print("\nAfter deleting at the beginning:")
dll.display_forward()

# Delete at end
dll.delete_at_end()
print("\nAfter deleting at the end:")
dll.display_forward()

# Delete at specific position
dll.delete_at_position(1)
print("\nAfter deleting at position 1:")
dll.display_forward()

# Display backward traversal to check links
print("\nBackward traversal after deletions:")
dll.display_backward()

dll.insert_at_position(50, 1)

# Display forward
dll.display_forward()

# Display backward
dll.display_backward()