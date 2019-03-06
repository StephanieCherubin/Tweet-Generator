from linkedlist import LinkedList
import time

#In hash tables, use l instead of n when speaking out big O notation
class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]
        self.count = 0

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []

        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

 
    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []

        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(b * l) or O(n) because it has to iterate through all bucket and count 1 for each"""
       
        count = 0

        for bucket in self.buckets:  # Loop through all buckets #b iterations
            count += bucket.length()  # Count number of key-value entries in each bucket #O(l)
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(1) Why and under what conditions?"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # Find method on linked_list is worst case: O(l)

        if entry:
            return True
        else:
            return False


    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        index = self._bucket_index(key)  # O(1) to calculate index
        bucket = self.buckets[index]  # O(1) to index an array
        
        def key_matcher(key_value):  # this function definition is a closure
            return (key_value[0] == key)  # just return the condition

        #Check if key-value entry exists in bucket
        entry = bucket.find(key_matcher)  # O(l) with l = bucket.length()
        # If found, return value associated with given key
        
        if entry is not None: # found!
            return entry[1]  # entry = (key, value)
        else: #Otherwise, raise error to tell user get failed
            raise KeyError('Key not found: {}'.format(key))
    

    def set(self, key, value):
        """Insert or update the given key with its associated value. 
        Running time: O(l) where l is the length of the linked list"""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        #  Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key) # O(l) with l = bucket.length()

        #If not found, update value associated with given key
        if entry: #entry = (key, value)
            # If found, return value associated with given key
            bucket.delete(entry) #O(l) where is the length of the linked list
            self.count -= 1

        bucket.append((key, value)) #O(1)
        self.count += 1 # Otherwise, insert given key-value entry into bucket
        # update key or set key if not there

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(3 + 2(l)) Why and under what conditions?"""
        # Find bucket where given key belongs
        index = self._bucket_index(key) # O(1)
        bucket = self.buckets[index]
        # bucket is linked_list
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        # Find method on linked_list is worst case: O(l)

        if entry: #If found
            bucket.delete(entry) #delete entry associated with given key
            # The delete method above is from linked_list class
            # O(l)
            self.count -= 1 #O(1)
        else: #Otherwise
            raise KeyError('Key not found: {}'.format(key)) # raise error to tell user delete failed

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()