from dataclasses import dataclass

# Understanding 'list', 'dict' and optional.
'''These are type hints also called type annotations from python's typing module.
What does it do?

It imports common type hints (List, Dict, Optional) from the typing module.

These are used to specify the expected types of variables, function parameters, and return values in Python 
code (especially useful for static type checkers like mypy).

As we know list and dict and optional is: 
Optional → Indicates that a value can be either of a given type or None.

( → ) This sign shows that what type of data they return. '''

# What is mypy?
'''Its a static type checker,analyzes the code without running it to check type related errors before execution'''
# e.g: 
'''Catches mismatches like passing a str to a function expecting an int.'''

# How to install?
'''pip install mypy
To run use:
mypy your_script.py'''

# What are nested data classes?
'''That contain other classes as fields, instead if storing all the data in a single flat structure, you 
organize related data into smaller, reusable data classes and then combine them heirarchically'''

# e.g:
'''@dataclass
class Address:
    street: str
    city: str

@dataclass
class Contact:
    email: str
    phone: str

@dataclass
class Employee:
    name: str
    address: Address   # Nested dataclass
    contact: Contact   # Nested dataclass'''

# Advantages:
'''Modular: Reuse Address/Contact in other classes.
Clear: Logical grouping (e.g., employee.address.city).
Maintainable: Change Address once, updates apply everywhere.'''

# How to Spot a Nested Dataclass
'''A dataclass field has another dataclass as its type'''

# Basically this is a nested dataclass:
'''@dataclass
class Employee:
    name: str
    age: int
    city: str
    country: str
    salary: int
@dataclass
class New_Employee:
    personal_info: Employee
    qualification: str

emp = Employee("John", 45 ,"Paris", "France", 3000000)

new_emp = New_Employee(emp, "PhD")
print(new_emp)'''
# output:
'''
New_Employee(personal_info=Employee(name='John', age=45, city='Paris', country='France', salary=3000000), 
qualification='PhD')  if you need multiline lookingg good output then we have to rewrite __repr__ in code'''
