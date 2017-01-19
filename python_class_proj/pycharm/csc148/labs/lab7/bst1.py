__author__ = 'zhangmohan'
class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every node, its value is >= all items stored in its left
    subtree, and < all items stored in its right subtree.
    """

    # === Private Attributes ===
    # @type _root: object
    #     The item stored at the root of the tree, or None if the tree is empty.
    # @type _left: BinarySearchTree | None
    #     The left subtree, or None if the tree is empty
    # @type _right: BinarySearchTree | None
    #     The right subtree, or None if the tree is empty

    # === Representation Invariants ===
    #  - If _root is None, then so are _left and _right. This represents an empty BST.
    #  - If _root is not None, then _left and _right are BSTs.
    #  - All items in _left are <= _root, and all items in _right are >= _root.

    def __init__(self, root):
        """Initialize a new BST with the given root value.

        If <root> is None, the tree is empty, and the subtrees are None.
        If <root> is not None, the subtrees are empty.

        @type self: BinarySearchTree
        @type root: object
            A value for the root of the BST. If None, the BST is empty.
        @rtype: None
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self):
        """Return True if self is empty.

        @type self: BinarySearchTree
        @rtype: bool

        >>> bst = BinarySearchTree(None)
        >>> bst.is_empty()
        True
        >>> bst = BinarySearchTree(10)
        >>> bst.is_empty()
        False
        """
        return self._root is None

    def print(self, depth=0):
        """Print all of the items in this BST,
        where the root is printed before all of its subtrees,
        and every value is indented to show its depth.

        @type self: BinarySearchTree
        @rtype: None
        """
        if not self.is_empty():
            print(depth * '  ' + str(self._root))
            self._left.print(depth + 1)
            self._right.print(depth + 1)

    def __contains__(self, item):
        """Return True if item is in this BST.

        @type self: BinarySearchTree
        @type item: object
        @rtype: bool

        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> 3 in bst
        True
        >>> 5 in bst
        True
        >>> 2 in bst
        True
        >>> 4 in bst
        False
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return item in self._left # or, self._left.__contains__(item)
        else:
            return item in self._right # # or, self._right.__contains__(item)

    # ------------------------------------------------------------------------
    # Lab 7 Exercises
    # ------------------------------------------------------------------------
    def height(self):
        """Return the height of this BST.

        @type self: BinarySearchTree
        @rtype: int

        >>> BinarySearchTree(None).height()
        0
        >>> bst = BinarySearchTree(7)
        >>> bst.height()
        1
        >>> bst._left = BinarySearchTree(5)
        >>> bst.height()
        2
        >>> bst._right = BinarySearchTree(9)
        >>> bst.height()
        2
        """
        # TODO
        if self.is_empty():
            return 0
        elif self._left.is_empty() and self._left.is_empty():
            return 1
        #elif self._left.is_empty() and not self._left.is_empty():
            #return 2
        #elif not self._left.is_empty() and self._left.is_empty():
            #return 2
        elif not self._left.is_empty() or not self._left.is_empty():
            return 1 + max(self._left.height(), self._right.height())

    def items(self):
        """Return all of the items in the BST in sorted order.

        @type self: BinarySearchTree
        @rtype: list

        >>> BinarySearchTree(None).items()
        []
        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items()
        [2, 3, 5, 7, 9, 11, 13]
        """
        # TODO
        if self.is_empty():
            return []
        elif self._left.is_empty() and self._right.is_empty():
            return [self._root]
        elif not self._left.is_empty() or not self._left.is_empty():
            return self._left.items() + [self._root] + self._right.items()

    def smaller(self, item):
        """Return all of the items in the BST strictly smaller than <item>
        in sorted order.

        @type item: object
        @rtype: list

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.smaller(6)
        [2, 3, 5]
        >>> bst.smaller(13)
        [2, 3, 5, 7, 9, 11]
        """
        # TODO 有问题！！
        if self.is_empty():
            return []
        else:
            if self._root == item:
                return self._left.items()
            elif self._root > item:
                if self._left._root < item:
                    return self._left.smaller(item)
                elif self._left._root >= item:
                    return self._left._left.smaller(item)
            elif self._root < item:
                return self._left.items() + [self._root] + self._right.smaller(item)

    def insert(self, item):
        """Insert <item> into this BST, maintaining the BST property.

        Do not change positions of any other items.

        @type self: BinarySearchTree
        @type item: object
        @rtype: None

        >>> bst = BinarySearchTree(10)
        >>> bst.insert(3)
        >>> bst.insert(20)
        >>> bst._root
        10
        >>> bst._left._root
        3
        >>> bst._right._root
        20
        """
        # TODO
        if self.is_empty():
            self._root = item
        elif self._root >= item:
            self._left.insert(item)
        elif self._root < item:
            self._right.insert(item)

    def rotate_right(self):
        """Rotate the BST clockwise, i.e. make the left subtree the root.

        @type self: BinarySearchTree
        @rtype: object

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> right = BinarySearchTree(11)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.print()
        7
          3
            2
            5
          11
        >>> bst.rotate_right()
        >>> bst.print()
        3
          2
          7
            5
            11
        >>> bst.rotate_right()
        >>> bst.print()
        2
          3
            7
              5
              11
        """
        # TODO
        root = BinarySearchTree(self._root)
        root._left = self._left._right
        root._right = self._right
        #self = self._left
        #self._right = root
        self._root = self._left._root
        self._left = self._left._left
        self._right = root
        """
        root = self
        pivot = self._left
        self._root = pivot._root
        self.left = pivot._left
        self._right = root
        root.left = pivot._right
        """

        pass
