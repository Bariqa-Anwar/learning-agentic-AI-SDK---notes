# from dataclasses import dataclass # built in python function, need to import at the time of usage(in line:5, 25... )
# from dataclasses import fields 
'''fields are blueprints you define in class
e.g: 
@dataclass
class Person:
    name: str      # ← This is a field definition
    age: int = 18  # ← This is also a field'''

# Data classes:
'''01: Dataclasses are a special feature in Python that make it easier to create classes that mainly store data. 
They automatically add common methods like __init__(), __repr__(), and __eq__() so you don't have to write 
them yourself.'''

#  __init__(), __repr__(), and __eq__()
'''02: These are special methods in Python classes, often called "magic methods" or "dunder methods"
(short for "double underscore")'''

'''1. __init__() - The Constructor
What it does:
It's automatically called when you create a new instance of a class
Used to initialize the object's attributes (set its initial state)'''

# e.g:
'''@dataclass
class Person:
    name: str   #__init__ is created automatically
    age: int
# works the same
p = Person("john", 25)  
print(p)  '''

# 2. __repr__ - The string representation
'''What it does?
. Returns a string that represents the object.
. Used when you print an object or look at it in the Python shell
. Should ideally be a string that could recreate the object'''
# e.g:
'''
@dataclass
class Person:   # just working behind the scenes thanks to the @dataclass decorator.
    name: str  
    age: int

p = Person("john", 25)  
print(p) 
it's just working behind the scenes thanks to the @dataclass decorator.
When you use @dataclass, Python automatically generates several special methods for you, including __repr__. 
You don't see it in your code because:

It's created automatically by the dataclass decorator
It follows a standard format showing the class name and all fields
It's implemented at the class level'''

# The Invisible __eq__ in Dataclasses
'''3. When you use @dataclass, Python automatically creates an __eq__ method that:

Checks if the compared object is the same type
Compares all fields you defined in the class
Returns True only if every field matches'''
# e.g:
'''@dataclass
class Person:
    name: str
    age: int
# Automatic __eq__ compares ALL fields
p1 = Person("John", 25)     
p2 = Person("John", 25)
p3 = Person("john", 20) 

print(p1 == p2)    # true for same name and age
print(p1 == p3)    # false (age differs)'''

# How it works behind the scenes?
'''def __eq__(self, other):
    if not isinstance(other, Person):
        return False
    return (self.name == other.name and 
            self.age == other.age)

When we say "behind the scenes" in dataclasses, we're talking about how Python rewrites your class at creation
time to inject these special methods.

# Where This Happens?
Location: In Python's class creation machinery (specifically in dataclasses._process_class())
When: When the @dataclass decorator runs (at module import time)
How: The decorator:
Collects all your type-annotated fields
Generates method source code as strings
Uses exec() to compile and inject them

# key points!
The methods exist in memory after class creation
They're not in your source file (the decorator adds them dynamically)
This is all part of Python's metaprogramming capabilities
The transformation happens exactly once, when Python loads your module'''

# So basically What Are Dataclasses?
'''Dataclasses are Python's way to quickly create classes that mainly store data. The @dataclass decorator 
automatically generates special methods like __init__() and __repr__() for you.'''