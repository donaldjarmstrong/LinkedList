from typing import Any

class Node:
    def __init__(self, data: Any, next: 'Node' = None) -> None:
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data: Any):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    # this is O(n)
    def size(self):
        count = 0
        node = self.head
        while (node != None):
            count += 1
            node = node.next
        return count

    def display(self):
        node = self.head
        while (node != None):
            if (node.next != None):
                print("{node.data} -> {node.next}")
            else:
                print(node.data)
            node = node.next

    def reverse(self):
        newList = LinkedList()
        tail = self.head
        while (tail != None):
            newList.add(tail.data)
            tail = tail.next
        return newList

mylist = LinkedList()
mylist.add(93)
mylist.add(87)
mylist.add(83)
mylist.add(54)
mylist.add(22)
mylist.display()

rev = mylist.reverse()
rev.display()
