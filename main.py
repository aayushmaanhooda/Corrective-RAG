import sys

class User:

    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("aayushmaan", 26)

# print(user)
# print("size", sys.getsizeof(user.__dict__))
print("size", sys.getsizeof(user.__dict__))
        