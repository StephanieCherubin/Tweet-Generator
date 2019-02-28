class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.count = 0

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node

        
        if items:
            for item in items:
                self.append(item) # Append given items

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(1) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time (constant time) to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time (constant time)to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        Running time: O(1)"""

        return self.head is None #

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Because we have to iterate through all nodes and count 1 for each"""
       
        length = 0
        node = self.head

        while node is not None: #Loop through all nodes
            length += 1  # and count one for each
            node = node.next
        return length
        # return self.length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1)
        Because the tail node is the only node changed and there is no loop."""
        
        new_node = Node(item) # Create new node to hold given item
        
        if self.tail:  # if there is a tail node   
            self.tail.next = new_node # add the new node after the tail node (last node)
        else: #tail contains no data
            self.head = new_node #make the new node the head because the test says so
        self.tail = new_node #in any case, the new node will be the last node


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) 
        Because we only change the first node and there is no loop."""
        
        new_node = Node(item) # Create new node to hold given item
        # TODO: Prepend node before head, if it exists

        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) If the item is near the head of the list
        Worst case running time: O(n) If the item is near the tail of the list
        where n = length of this linked list (number of items it stores)"""
        
        
        node = self.head
    
        while node is not None: # Loop through all nodes to find item where quality(item) is True
            if quality(node.data): # quality is a function that needs to be called if True
                #Check if node's data satisfies given quality function
                return node.data
            else:
                node = node.next
        return None 

    def replace(self, word, replacement):
        """Replace method deletes an existing item and replaces it with a new item,
        without creating a new node."""
        
        node = self.head
        # Loop through all nodes. If the (node.data) == word, replace with replacement
        while node: # check if head exists
            if node.data == word:
                node.data = replacement
            else:
                node = node.next
        

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) Why and under what conditions?
        TODO: Worst case running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data


        node = self.head
        previous_node = None
        found = False
        
        #  The linkedlist only has a single node
        if self.head == self.tail: # check if the head node is the only node
        # remove it, and set self.head to None, and self.tail to None
             self.head = None
             self.tail = None
        
        # The linkedlist has at least a head and a tail
        while node: #while the head node exists

         # The data has been found
            if node.data == item: 
                if previous_node is not None: #
                    previous_node.next = node.next
                    found = True

                else: #head_node
                    self.head = node.next
                    found = True

                if node.next == None: #tail
                    self.tail = previous_node
                break
            
            else: # The data has not been found, so look at next node
                previous_node = node
                node = node.next
        if not found: #Otherwise raise error to tell user that delete has failed
            raise ValueError('Item not found: {}'.format(item))



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

        # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None 
        return 
    
    def add_item(self, item):
        if self.head is None:
            self.head = item 
            item.prev = None 
            item.next = None 
            self.tail = item 
        else:
            self.tail.next = item 
            item.prev = self.tail 
            self.tail = item

if __name__ == '__main__':
    test_linked_list()