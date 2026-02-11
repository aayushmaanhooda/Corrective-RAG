import sys

# Without __slots__ - The RAM hog
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

# With __slots__ - The memory-efficient version
class OptimizedUser:
    __slots__ = ['name', 'email']
    
    def __init__(self, name, email):
        self.name = name
        self.email = email


user1 = User("aayushmaan", 26)
user2 = OptimizedUser("aayushmaan", 26)

# Get memory in bytes
memory_without_slots = sys.getsizeof(user1.__dict__)
memory_with_slots = sys.getsizeof(user2)

print(f"Memory used without __slots__: {memory_without_slots} bytes ({memory_without_slots / 1024:.2f} KB)")
print(f"Memory used with __slots__: {memory_with_slots} bytes ({memory_with_slots / 1024:.2f} KB)")
print(f"Memory saved: {memory_without_slots - memory_with_slots} bytes ({(memory_without_slots - memory_with_slots) / 1024:.2f} KB)")
print(f"Reduction: {((memory_without_slots - memory_with_slots) / memory_without_slots * 100):.1f}%")