class Node:
    def __init__(self, data):
        self.data = data  # Store node's data
        self.next = None  # Initialize next as None


class Queue:
    def __init__(self):
        self.front = None  # Pointer to the front of the queue
        self.rear = None   # Pointer to the rear of the queue

    def enqueue(self, data):
        """Add an element to the end of the queue"""
        new_node = Node(data)
        if self.rear is None:  # If the queue is empty
            self.front = self.rear = new_node  # Both front and rear point to the new node
        else:
            self.rear.next = new_node  # Link the current rear to the new node
            self.rear = new_node       # Update rear to the new node

    def dequeue(self):
        """Remove and return the front element of the queue"""
        if self.is_empty():
            print("Queue is empty. No elements to dequeue.")
            return None
        dequeued_data = self.front.data  # Retrieve data from the front node
        self.front = self.front.next     # Move front to the next node

        if self.front is None:  # If queue becomes empty after dequeue
            self.rear = None    # Update rear to None as well

        return dequeued_data

    def peek(self):
        """Return the front element without removing it"""
        if self.is_empty():
            print("Queue is empty. No elements to peek.")
            return None
        return self.front.data

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None

    def display(self):
        """Display the queue from front to rear"""
        current = self.front
        print("Queue (front to rear):")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
queue = Queue()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
print("After enqueuing elements:")
queue.display()

# Peek at the front element
print("Front element (peek):", queue.peek())

# Dequeue elements
print("Dequeued element:", queue.dequeue())
print("After dequeuing one element:")
queue.display()

# Check if the queue is empty
print("Is the queue empty?", queue.is_empty())

# Dequeue remaining elements
queue.dequeue()
queue.dequeue()
print("After dequeuing all elements:")
queue.display()
print("Is the queue empty?", queue.is_empty())
