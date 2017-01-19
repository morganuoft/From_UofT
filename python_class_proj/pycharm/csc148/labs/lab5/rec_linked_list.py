class LinkedListRec:
    """A recursive linked list implementation of the List ADT.

    Note the structural differences between this implementation
    and the node-based implementation from last week. Even though
    both classes have the same public interface, how they
    implement their methods are quite different!

    There is no "_Node" class with this implementation.
    """
    # === Private Attributes ===
    # @type _first: object | None
    # @type _rest: LinkedListRec | None
    #     A list containing the other items after the first one.
    #
    # === Representation Invariants ===
    # - _first is None if and only if _rest is None. This situation
    #   represents an empty list.

    def __init__(self, items):
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.

        @type self: LinkedListRec
        @type items: list
        @rtype: None
        """
        if len(items) == 0:
            self._first = None
            self._rest = None
        else:
            self._first = items[0]
            self._rest = LinkedListRec(items[1:])

    def is_empty(self):
        """Return whether this linked list is empty.

        @type self: LinkedListRec
        @rtype: bool
        """
        return self._first is None

    def __str__(self):
        """Return a string representation of this list..

        @type self: LinkedListRec
        @rtype: str

        >>> lst = LinkedListRec([1, 2, 3])
        >>> str(lst) # Equivalent to lst.__str__()
        '1 -> 2 -> 3'
        """
        if self.is_empty():
            return ''
        elif self._rest.is_empty():
            return str(self._first)
        else:
            return str(self._first) + ' -> ' + str(self._rest)

    def __len__(self):
        """Return the number of elements in this list.

        @type self: LinkedListRec
        @rtype: int

        >>> lst = LinkedListRec([])
        >>> len(lst) # Equivalent to lst.__len__()
        0
        >>> lst = LinkedListRec([1, 2, 3])
        >>> len(lst)
        3
        """
        # TODO: complete this function!
        if self._first is None:
            return 0
        elif self._rest is None:
            return 1
        elif self._rest is not None:
            a = 1
            a = a + len(self._rest)
        return a

    def __getitem__(self, index):
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        @type self: LinkedListRec
        @type index: int
        @rtype: object

        >>> lst = LinkedListRec([1, 2, 3])
        >>> lst[0] # Equivalent to lst.__getitem__(0)
        1
        >>> lst[1]
        2
        >>> lst[2]
        3
        >>> lst[3]
        Traceback (most recent call last):
        ...
        IndexError
        """
        if self.is_empty():
            raise IndexError
        elif index == 0:
            return self._first
        else:
            return self._rest.__getitem__(index - 1)
            # Equivalently, return self._rest[index - 1]

    def __setitem__(self, index, item):
        """Store item at position <index> in this list.

        Raise IndexError if index is >= the length of <self>.

        @type self: LinkedListRec
        @type index: int
        @type item: object
        @rtype: None

        >>> lst = LinkedListRec([1, 2, 3])
        >>> lst[0] = 100 # Equivalent to lst.__setitem__(0, 100)
        >>> lst[1] = 200
        >>> lst[2] = 300
        >>> lst[3] = 400
        Traceback (most recent call last):
        ...
        IndexError
        >>> str(lst)
        '100 -> 200 -> 300'
        """
        # TODO: complete this function!
        if self.is_empty():
            raise IndexError
        elif index == 0:
            self._first = item
        else:
            self._rest[index - 1] = item

    def __contains__(self, item):
        """Return whether <item> is in this list.

        Use == to compare items.

        @type self: LinkedListRec
        @type item: object
        @rtype: bool

        >>> lst = LinkedListRec([1, 2, 3])
        >>> 2 in lst # Equivalent to lst.__contains__(2)
        True
        >>> 4 in lst
        False
        """
        if self.is_empty():
            return False
        elif self._first == item:
            return True
        else:
            return self._rest.__contains__(item)
            # Equivalently, item in self._rest

    def count(self, item):
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        @type self: LinkedListRec
        @type item: object
        @rtype: int

        >>> lst = LinkedListRec([1])
        >>> lst.count(1)
        1
        >>> lst = LinkedListRec([2])
        >>> lst.count(1)
        0
        >>> lst1 = LinkedListRec([1, 2])
        >>> lst1.count(1)
        1
        >>> lst1 = LinkedListRec([1, 2, 1])
        >>> lst1.count(1)
        2
        >>> lst = LinkedListRec([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        # TODO: complete this function!

        if self._first is None:
            return 0
        elif self._first != item and len(self._rest) == 0:
            return 0
        elif self._first == item and len(self._rest) == 0:
            return 1
        elif self._first == item and len(self._rest) != 0:
            return 1 + self._rest.count(item)
        elif self._first != item and len(self._rest) != 0:
            return 0 + self._rest.count(item)

    # ------------------------------------------------------------------------
    # Mutating methods: these methods modify the structure of the list
    # ------------------------------------------------------------------------

    def remove_first(self):
        """Remove the first item in the list.

        Raise an IndexError if the list is empty.

        @type self: LinkedListRec
        @rtype: None

        >>> lst = LinkedListRec([1, 2, 3])
        >>> lst.remove_first()
        >>> str(lst)
        '2 -> 3'
        >>> lst.remove_first()
        >>> str(lst)
        '3'
        >>> lst.remove_first()
        >>> str(lst)
        ''
        """
        pass

    def insert_first(self, item):
        """Insert item at the front of the list.

        This should work even if the list is empty.

        @type self: LinkedListRec
        @rtype: None

        >>> lst = LinkedListRec([])
        >>> lst.insert_first(3)
        >>> str(lst)
        '3'
        >>> lst.insert_first(2)
        >>> str(lst)
        '2 -> 3'
        >>> lst.insert_first(1)
        >>> str(lst)
        '1 -> 2 -> 3'
        """
        pass

    def remove(self, index):
        """Remove node at position <index>.

        Raise IndexError if <index> is >= the length of this list.

        @type self: LinkedListRec
        @type index: int
        @rtype: None

        >>> lst = LinkedListRec([1, 2, 3])
        >>> lst.remove(2)
        >>> str(lst)
        '1 -> 2'
        >>> lst.remove(1)
        >>> str(lst)
        '1'
        >>> lst.remove(0)
        >>> str(lst)
        ''
        >>> lst.remove(0)
        Traceback (most recent call last):
        ...
        IndexError
        """
        pass

    def insert(self, index, item):
        """Insert item in to the list at position <index>.

        Raise an IndexError if index is > the length of the list.
        Note that it is possible to add to the end of the list
        (when index == len(self)).

        @type self: LinkedListRec
        @type index: int
        @rtype: None

        >>> lst = LinkedListRec(['c'])
        >>> lst.insert(0, 'a')
        >>> str(lst)
        'a -> c'
        >>> lst.insert(1, 'b')
        >>> str(lst)
        'a -> b -> c'
        >>> lst.insert(3, 'd')
        >>> str(lst)
        'a -> b -> c -> d'
        >>> lst.insert(5, 'd')
        Traceback (most recent call last):
        ...
        IndexError
        """
        pass

    # --- Additional Exercises ---

    def map(self, f):
        """Return a new LinkedList whose nodes store items that are
        obtained by applying f to each item in this linked list.

        Does not change this linked list.

        @type self: LinkedListRec
        @type f: Function
        @rtype: LinkedListRec

        >>> func = str.upper
        >>> func('hi')
        'HI'
        >>> lst = LinkedListRec(['Hello', 'Goodbye'])
        >>> str(lst.map(func))
        'HELLO -> GOODBYE'
        >>> str(lst.map(len))
        '5 -> 7'
        """
        pass

def insert_sorted(lst, item):
    if lst.is_empty():
        lst._first = item
        lst._rest = LinkedListRec([])
    elif lst._first >= item:
        #new_rec_list = LinkedListRec([lst._first])
        #new_rec_list._rest = lst
        #lst._first = item
        #lst._rest = new_rec_list
        new_rec_list = LinkedListRec([lst._first])
        new_rec_list._rest = lst._rest
        lst._first = item
        lst._rest = new_rec_list
    else:
        insert_sorted(lst._rest, item)




