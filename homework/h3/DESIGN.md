> HW3 Design Document

## def __str__(self):
    """
    Create string representation of the unordered list object. The string
    shows the data items, separated by ','. If the list is empty, the
    string is empty string.
    :return: string
    """
### Problem Solving Steps
- Create an empty list `items` to store the data items as strings.
- Initialize a reference `current` to the first node in the list.
- Use a `while` loop to iterate through the nodes in the list.
    - Check if the `current` node is not `None`
    - Inside the loop, get the data from the `current` node using the `get_data` method, 
      convert it to a string, and append it to the `items` list.
    - Move to the next node in the list by updating `current` to be the node linked 
      to the current node using the `get_next` method.
- After processing all nodes in the list, return a string created by joining all the `items` in the items list 
with ',' as the separator.
- End the method.

## def append(self, item):
    """
    Append a new node containing the specified item to the end of the unordered list.
    :param item: The item to be appended to the list
    :param: any
    """
### Problem Solving Steps
- Create a new node named `new_node` that contains the specified `item`.
- Check if the list is empty by verifying whether `self.head` is `None`.
    - If the list is empty, set `self.head` to the new node `new_node`.
    - This makes `new_node` the first and only node in the list since the 
      list was initially empty.
- If the list is not empty, it means there are existing nodes in the list.
- Initialize a reference named `current` to the first node in the list.
- Use a `while` loop to iterate through the list to find the last node.
- Inside the loop, check if the current node has a next node by 
using the `get_next` method.
    - If there's a next node, update the `current` reference to be the next node.
- When the loop ends, the `current` reference will be pointing to the last node in the list.
- Set the next node of the last node to be the new node `new_node` 
using the `set_next` method.
- End the method.

## def pop(self):
    """
    Remove and return the first node in the unordered list. If the list is empty, return None.
    :return: The data item in the removed node or None if the list is empty
    :return: any | None
    """
### Problem Solving Steps
- Check if the list is empty by using the `is_empty` method.
    - If the list is empty, return `None` because there are no nodes to remove.
- If the list is not empty:
    - Get the data from the first node, which is stored in the `head` 
      of the list, using the `get_data` method. This data will be removed and returned.
    - Update the `head` of the list to point to the next node in the list using the `get_next` method.
    - Return the removed data item.
- End the method.

## def remove(self, item):
    """
    Remove the node containing the specified item from the unordered list.
    If the item is removed successfully, return the removed item. If not found, return None.
    :param item: The item to be removed from the list
    :param: any
    :return: The removed item or None if the item is not found
    :return: any | None
    """
### Problem Solving Steps
- Check if the list is empty by using the `is_empty` method.
- If the list is empty, return `None`
- If the list is not empty, start iterating through the nodes in the list:
    - Initialize a reference `current` to the first node in the list and `previous` to `None`.
    - Use a `while` loop to iterate the list.
    - Inside the loop, check if the data in the `current` node matches 
      the specified `item` that you want to remove.
        - If there's a match, it means you've found the node to remove:
            - Check if there's a previous node.
                - If there's a previous node, set the `next`
                  of the previous node to point to the node following the `current` node.
                - This effectively removes the `current` node from the list.
                - If there's no previous node, it means the `current` node is the first node
                    - Update the `self.head` to point to the next node in the list, 
                      effectively removing the first node.
            - Return the `item` that was successfully removed.
        - If there's no match, continue iterating by updating `previous` to `current` 
          and `current` to the next node using the `get_next` method.
- If the loop completes without finding the specified `item`, 
it means the item is not in the list, so return `None` 
to indicate that the item was not found and not removed.
- End the method.