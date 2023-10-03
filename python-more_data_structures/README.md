## Python Data Structures

Data structures are "containers" that organize and group data according to type. The fundamental data structures in Python are list, set, tuples, and dictionary, each of which is distinct in its own way.


On the basis of order and mutability, the data structures differ. An object's mutability is its capacity for modification after creation. After being created, mutable objects can be changed, expaded, or removed, whereas immutable objects cannot be changed. Order, in this context, relates to whether the position of an element can be used to access the element.


### Python Data Structures – Lists
A list is defined as an ordered collection of items. Lists are defined by using parentheses to enclose the elements, which are separated by commas. A sample list can be written as follows:

List_A = [item 1, item 2, item 3….., item n]

# Lists can be nested
 It can include another list or a sublist – which can subsequently contain other sublists itself. There is no limit to the depth with which lists can be nested.

Lists are mutable: Lists created in Python qualify to be mutable because they can be altered even after being created.

### Python Data Structures – Tuples
Unlike lists, tuples come with limited functionality. The primary differing characteristic between lists and tuples is mutability. Lists are mutable, whereas tuples are immutable. Tuples cannot be modified, added, or deleted once they’ve been created.

Sometimes, the user can create an object that is intended to remain intact during its lifetime. Tuples are immutable, so they can be used to prevent accidental addition, modification, or removal of data.


### Python Data Structures – Sets

A set is referred to as unique grouping of distinct elements that do not have a predetermined order. Unlike tuples, sets are mutable. A sample set can be represented as follows:

set_a = {“item 1”, “item 2”, “item 3”,….., “item n”}


### Dictionaries:
Dictionaries are collections of key-value pairs. Each key in the dictionary maps to a corresponding value. Dictionaries are useful for quick lookups based on keys. They are denoted by curly braces {} with key-value pairs separated by colons:.
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

Dictionaries are written with curly brackets, and have keys and values:

Example
Create and print a dictionary:

ph_dict = {
  "brand": "Tecno",
  "model": "Camon 20",
  "year": 2023
}
print(ph_dict)

