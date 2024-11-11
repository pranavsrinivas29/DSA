class Node:
    def __init__(self, data):
        self.data = data  # Store node's data
        self.next = None  # Initialize next as None


class Stack:
    def __init__(self):
        self.top = None  # Initialize the top of the stack as None

    def push(self, data):
        """Add an element to the top of the stack"""
        new_node = Node(data)      # Create a new node with the given data
        new_node.next = self.top   # Link the new node to the current top
        self.top = new_node        # Update the top to the new node

    def pop(self):
        """Remove and return the top element from the stack"""
        if self.is_empty():
            print("Stack is empty. No elements to pop.")
            return None
        popped_data = self.top.data  # Retrieve data from the top node
        self.top = self.top.next     # Move the top pointer to the next node
        return popped_data

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            print("Stack is empty. No elements to peek.")
            return None
        return self.top.data

    def is_empty(self):
        """Check if the stack is empty"""
        return self.top is None

    def display(self):
        """Display the stack from top to bottom"""
        current = self.top
        print("Stack (top to bottom):")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
stack = Stack()

# Push elements
stack.push(10)
stack.push(20)
stack.push(30)
print("After pushing elements:")
stack.display()

# Peek at the top element
print("Top element (peek):", stack.peek())

# Pop elements
print("Popped element:", stack.pop())
print("After popping one element:")
stack.display()

# Check if the stack is empty
print("Is the stack empty?", stack.is_empty())

# Pop remaining elements
stack.pop()
stack.pop()
print("After popping all elements:")
stack.display()
print("Is the stack empty?", stack.is_empty())
