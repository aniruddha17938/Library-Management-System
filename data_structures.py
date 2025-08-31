# data_structures.py
from collections import deque

class Book:
    def __init__(self, id, title, author, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.available = available

class Node:
    def __init__(self, book):
        self.book = book
        self.next = None

class Category:
    def __init__(self, name):
        self.name = name
        self.head = None

    def add_book(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node

    def list_books(self):
        books = []
        current = self.head
        while current:
            books.append(vars(current.book))
            current = current.next
        return books

class LibraryGraph:
    def __init__(self):
        self.categories = {}

    def add_category(self, name):
        if name not in self.categories:
            self.categories[name] = Category(name)

    def get_all_books(self):
        all_books = {}
        for name, category in self.categories.items():
            all_books[name] = category.list_books()
        return all_books

class Waitlist:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, user):
        self.queue.append(user)

    def dequeue(self):
        return self.queue.popleft() if self.queue else None
