class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node

        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        
        if self.tail is not None:  # if there is a tail node   
            self.tail.next = new_node # add the new node after the tail node (last node)
        else: #tail contains no data
            self.head = new_node #make the new node the head because the test says so
        self.tail = new_node #in any case, the new node will be the last node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists

        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        node_node = self.head

        while node_node is not None:
            if quality(node_node.data):
                return node_node.data
            else:
                node_node = node_node.next
        return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        node = self.head
        prev = None

        while node is not None : #while the head node exists
            print('Node.data: {}'.format(node.data))

            if node.data == item: #if the data of the head node is the item
                if prev is not None: #if previous node exists
                    prev.next = node.next #set the previous node to the head node.next
                    node = node.next
                else:
                    self.head = node.next #head node is now moved to the next one.
                    node = node.next
            else:
                print('Node.data: {}'.format(node.data))
                prev = node
                node = node.next
                if node.next == None:
                    node = None
        raise ValueError('Item not found: {}'.format(item))


def test_linked_list():
    singly_linked_list = LinkedList()
    print('list: {}'.format(singly_linked_list))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        singly_linked_list.append(item)
        print('list: {}'.format(singly_linked_list))

    print('head: {}'.format(singly_linked_list.head))
    print('tail: {}'.format(singly_linked_list.tail))
    print('length: {}'.format(singly_linked_list.length()))

        # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            singly_linked_list.delete(item)
            print('list: {}'.format(singly_linked_list))

        print('head: {}'.format(singly_linked_list.head))
        print('tail: {}'.format(singly_linked_list.tail))
        print('length: {}'.format(singly_linked_list.length()))


# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None 
#         return 
    
#     def add_item(self, item):
#         if self.head is None:
#             self.head = item 
#             item.prev = None 
#             item.next = None 
#             self.tail = item 
#         else:
#             self.tail.next = item 
#             item.prev = self.tail 
            # self.tail = item

if __name__ == '__main__':
    test_linked_list()