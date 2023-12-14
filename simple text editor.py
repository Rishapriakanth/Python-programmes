class CustomStack:
    def __init__(self):
        self.text = ""
        self.history = []

    def insert(self, value):
        self.text += value
        self.history.append(("insert", value))

    def delete(self, value):
        deleted_text = self.text[-value:]
        self.text = self.text[:-value]
        self.history.append(("delete", deleted_text))

    def get(self, value):
        char = self.text[value - 1]
        print(char)

    def undo(self):
        if self.history:
            last_operation, last_value = self.history.pop()
            if last_operation == "insert":
                self.text = self.text[:-len(last_value)]
            elif last_operation == "delete":
                self.text += last_value

user_input_1 = input()
commands1 = user_input_1.split(",")
editor1 = CustomStack()
for command in commands1:
    cmd, *args = command.split()
    if cmd == "1":
        editor1.insert(args[0])
    elif cmd == "2":
        editor1.delete(int(args[0]))
    elif cmd == "3":
        editor1.get(int(args[0]))

