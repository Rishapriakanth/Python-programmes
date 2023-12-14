import sys

class CustomQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

    def print_front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2[-1]


user_input_1 = input()
queries1 = user_input_1.split(",")
queue1 = CustomQueue()
for query in queries1:
    query_type, *args = map(int, query.split())
    if query_type == 1:
        queue1.enqueue(args[0])
    elif query_type == 2:
        queue1.dequeue()
    elif query_type == 3:
        print(queue1.print_front())

