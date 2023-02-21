# STACK:: AKHARIN VORODI, MISHE AVVALIN KHOROJI.
# behtarin mesal bara stack:: dokme back e to computer ke mizani mire qabli folder.


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push_(self, value):
        self.list.append(value)
        return " created."

    def pop(self):
        if self.isEmpty():
            return "there is no list in here"
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "there is no list in here"
        return self.list[len(self.list) - 1]

    def delete(self):
        self.list = None


custom = Stack()
custom.push_(1)
custom.push_(2)
custom.push_(3)
print(custom)

custom.pop()
print(custom)

# print(custom.isEmpty())

print(custom.peek())
