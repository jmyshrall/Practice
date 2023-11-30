"""
unorderedlist.py
Jon Shallow
20231102
"""

from node import Node


class UnorderedList:
    """
    Class representation of an UnorderedList
    """

    def __init__(self):
        """
        Constructor
        """
        self.head = None

    def prepend(self, item):
        """
        Create node that has item and make it the first element in the
        unordered list.
        :param item: integer
        """
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        """
        Count the number of elements in the unordered list.
        :return: integer
        """
        count = 0
        curr_node = self.head
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def is_empty(self):
        """
        Check whether the unordered list has no nodes.
        :return: True if the unordered list object doesn't have any element.
        """
        return self.head is None

    def search(self, item):
        """
        Search for item in the unordered list.
        :param item: integer
        :return: True if item found. False otherwise.
        """
        curr_node = self.head
        while curr_node:
            if curr_node.get_data() == item:
                return True
            curr_node = curr_node.get_next()
        return False

    def __str__(self):
        """
        Create string representation of the unordered list object. The string
        shows the data items, separated by ','. If the list is empty, the
        string is empty string.
        :return: string
        """
        items = []
        current = self.head
        while current:
            items.append(str(current.get_data()))
            current = current.get_next()
        return ",".join(items)
        pass

    def append(self, item):
        """
        Append a new node containing the specified item to the end of the unordered list.
        :param item: The item to be appended to the list
        :param: any
        """

        new_node = Node(item)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)

        pass

    def pop(self):
        """
        Remove and return the first node in the unordered list. If the list is empty, return None.
        :return: The data item in the removed node or None if the list is empty
        :return: any | None
        """

        if self.is_empty():
            return None
        removed_item = self.head.get_data()
        self.head = self.head.get_next()
        return removed_item

        pass

    def remove(self, item):
        """
        Remove the node containing the specified item from the unordered list.
        If the item is removed successfully, return the removed item. If not found, return None.
        :param item: The item to be removed from the list
        :param: any
        :return: The removed item or None if the item is not found
        :return: any | None
        """
        if self.is_empty():
            return None

        current = self.head
        previous = None

        while current:
            if current.get_data() == item:
                if previous:
                    previous.set_next(current.get_next())
                else:
                    self.head = current.get_next()
                return item
            previous = current
            current = current.get_next()

        return None

        pass
