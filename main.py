"""
A Linked List Example
"""
from linked_list import LinkedList

if __name__ == '__main__':
    a_list = LinkedList('Ant')
    a_list.append('Bat')
    a_list.append('Cat')
    a_list.append('Dog')
    print(a_list)
    print(len(a_list))

    for item in a_list:
        print(item, end=" ")
    print()

    a_list.remove(0)
    print(a_list)
    print(len(a_list))

    a_list.remove(1)
    print(a_list)
    print(len(a_list))

    a_list.insert(0, 'Ant')
    a_list.insert(2, 'Cat')
    a_list.insert(5, 'Elephant')
    print(a_list)

    for idx, item in enumerate(a_list):
        print(idx, item)
    print()
