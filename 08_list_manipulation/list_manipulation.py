def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    command1 = "add"
    command2 = "remove"
    location1 = "beginning"
    location2 = "end"

    if command == command1:
        if location == location1:
            lst.insert(0, value)
        elif location == location2:
            lst.append(value)
        print (lst)
    elif command == command2:
        if location == location1:
            lst.pop(0)
        elif location == location2:
            lst.pop()
        print (lst)

lst = [1, 2, 3]
list_manipulation(lst, 'remove', 'end')
list_manipulation(lst, 'remove', 'beginning')
list_manipulation(lst, 'add', 'beginning', 20)
list_manipulation(lst, 'add', 'end', 30)
list_manipulation(lst, 'foo', 'end') is None
list_manipulation(lst, 'add', 'dunno') is None

