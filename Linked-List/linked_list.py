class Node:
    def __init__(self, value):
        self.value=value
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None

    def append(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node
        else:
            current=self.head
            while current.next!=None:
                current=current.next
            current.next=new_node


    def traverse(self):
        if not self.head:
            print("Single Linked list is empty")
        else:
            current=self.head
            while current is not None:
                print(current.value, end=" -> " if current.next else "")
                current=current.next
            print()

    def insert_at(self, value, position):
        new_node=Node(value)
        if position<0:
            print("Position cannot be negative")
            return
        if position > self.length():
            print("Position out of bounds")
            return
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current is not None and count < position:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current
        print(f"Inserted {value} at position {position}:")
        self.traverse()    

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

  
    def delete(self, value):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return

        # Case 1: Head node is the one to delete
        if self.head.value == value:
            self.head = self.head.next
            print(f"Deleted node with value {value} (was head)")
            self.traverse()
            return

        # Case 2: Search for the node
        current = self.head
        prev = None
        while current is not None and current.value != value:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {value} not found.")
            return

        # Delete the node
        prev.next = current.next
        print(f"Deleted node with value {value}")
        self.traverse()
    
    def delete_at(self, index):
        if index < 0:
            print("Index cannot be negative.")
            return

        if self.head is None:
            print("List is empty. Nothing to delete.")
            return

        if index >= self.length():
            print("Index out of bounds.")
            return

        # Deleting head
        if index == 0:
            print(f"Deleted node at index {index} with value {self.head.value}")
            self.head = self.head.next
            self.traverse()
            return

        # Traverse to node before the one to delete
        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.next
            count += 1

        # current is now at (index - 1)
        if current.next is not None:
            deleted_value = current.next.value
            current.next = current.next.next
            print(f"Deleted node at index {index} with value {deleted_value}")
        else:
            print("Unexpected error: next node is None.")

        self.traverse()

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next   # Store next node
            current.next = prev        # Reverse the link
            prev = current             # Move prev forward
            current = next_node        # Move current forward

        self.head = prev
        print("Reversed linked list:")
        self.traverse()

    def find_middle(self):
        if self.head is None:
            print("List is empty.")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(f"The middle element is: {slow.value}")


sll=Linked_List()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()
sll.insert_at(1,1)
sll.delete(30)  # Should delete 30 and show the updated list
sll.delete(100) # Should print "Node with value 100 not found."
sll.delete(10)  # Should delete the head
sll.traverse()  # Final state of the list
sll.delete_at(2)  # Deletes the node with value 30
sll.delete_at(0)  # Deletes the head node (10)
sll.delete_at(10) # Index out of bounds

sll = Linked_List()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.traverse()         # Output: 10 -> 20 -> 30 -> 40

sll.reverse()          # Output: 40 -> 30 -> 20 -> 10
length=sll.length()
print(f"the total length:{length}")
sll.find_middle()
