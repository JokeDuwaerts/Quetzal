class _Node:
    def __init__(self, item, prev, next):
        """ Creates new node.

        :param item: Item that contains data.
        :param prev: Previous node.
        :param next:  Next node.
        """
        self.item = item
        self.prev = prev
        self.next = next


class AdtDoublyLinkedList:
    def __init__(self):
        """
        Creates a new doubly linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def __del__(self):
        """
        Destroys the current double linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def is_empty(self):
        """ Checks if a list is empty.

        :return: Boolean: If the list is empty or not.
        """
        return self.length == 0

    def get_length(self):
        """ Returns the length of the list

        :return: The length of the list
        """
        return self.length

    def __setitem__(self, index, new_item):
        """ Inserts a node into a given location.

        :param index: The index to insert into
        :param new_item: The item to insert
        :return: Boolean: If the insertion succeeded
        """
        if self.head is None or index == 0:
            return self._insert_beginning(new_item)
        elif index > self.length:
            return self._insert_end(new_item)
        else:
            current_node = self._search_node(index - 1)
            new_node = _Node(new_item, current_node, current_node.next)
            # Correct the prev from the node after the new node
            current_node.next.prev = new_node
            # Correct the next from the node before the new node
            current_node.next = new_node
            self.length += 1
            return True

    def _insert_beginning(self, new_item):
        """
        Inserts a node at the beginning of the list.
        :param new_item: The item to insert
        :return: Boolean: If the insertion succeeded
        """
        new_node = _Node(new_item, None, self.head)
        if self.head is not None:
            self.head.prev = new_node
            self.tail = self.head
        self.head = new_node
        self.length += 1
        return True

    def _insert_end(self, new_item):
        """
        Inserts a node at the end of the list.
        :param newItem: The item to insert
        :return: Boolean: If the insertion succeeded
        """
        if self.head is None:
            return self._insert_beginning(new_item)
        else:
            last_node = self._search_node(self.length)
            new_node = _Node(new_item, last_node, None)
            last_node.next = new_node
            self.tail = new_node
            self.length += 1
            return True

    def __delitem__(self, key):
        """
        Deletes a node from the list.
        :param index: The index of the node that needs to be removed
        :return: Boolean: If the insertion succeeded
        """
        if index < 1:
            index = 1
        if index > self.get_length():
            index = self.get_length()

        deleted_node = self._search_node(index)
        before_node = deleted_node.prev
        after_node = deleted_node.next

        if index == 1:
            self.head = after_node
        if before_node is not None:
            before_node.next = after_node
        if after_node is not None:
            after_node.prev = before_node

        self.length -= 1
        return True

    def __getitem__(self, item):
        """
        Deletes a node from the list and returns the data from the node.
        :param index: The index of the node that needs to be retrieved
        :return: The retrieved item
        :return: Boolean: If the insertion succeeded
        """
        if index < 1:
            index = 1
        if index > self.get_length():
            index = self.get_length()

        deleted_node = self._search_node(index)
        before_node = deleted_node.prev
        after_node = deleted_node.next

        if index == 1:
            self.head = after_node
        if before_node is not None:
            before_node.next = after_node
        if after_node is not None:
            after_node.prev = before_node

        self.length -= 1
        return deleted_node.item, True

    def _search_node(self, index):
        """
        Searches the location of the node just before the given index.
        :param index: The index of the node to search
        :return: The found node
        """
        i = 0
        current_node = self.head

        while i < index - 1:
            current_node = current_node.next
            i += 1

        return current_node

    def _search_item(self, index):
        result = self._search_node(index)

        if result is None:
            return None, False
        else:
            return result.item, True
