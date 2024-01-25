"""
A Linked List Example
"""
from linked_list import LinkedList

if __name__ == '__main__':
    # This part is to create a LinkedList object with the first node as 'Ant'.
    # And then it adds 'Bat', 'Cat' and 'Dog'.
    a_list = LinkedList('Ant')
    a_list.append('Bat')
    a_list.append('Cat')
    a_list.append('Dog')

    # Print the list and the length of it
    print(a_list)
    print(len(a_list))

    # # Commented out the debug for loop.
    # for item in a_list:
    #     print(item, end=" ")
    # print()

    # Remove the node at index 0 and print the list and its length.
    a_list.remove(0)
    print(a_list)
    print(len(a_list))

    # Remove the node at index 1 and print the list and its length.
    a_list.remove(1)
    print(a_list)
    print(len(a_list))

    # Insert 'Ant', 'Cat' and 'Elephant' to the list at index 0, 2 and 5.
    a_list.insert(0, 'Ant')
    a_list.insert(2, 'Cat')
    a_list.insert(5, 'Elephant')
    print(a_list)

    # Test the function enumerate with the LinkedList object.
    for idx, item in enumerate(a_list):
        print(idx, item)
    print()
