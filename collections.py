# https://docs.python.org/3/library/collections.html
from collections import deque 
from collections import Counter
from collections import defaultdict
import collections

################################################################################################
#  collections.deque : list-like container with fast appends and pops on either end

cities_list =  deque(["London", "Berlin", "Paris", "Madrid", "Rome", "Moscow"])
cities_list.appendleft('Mumbai') 
print(cities_list)      # deque(['Mumbai', 'London', 'Berlin', 'Paris', 'Madrid', 'Rome', 'Moscow'])
cities_list.pop()
print(cities_list)      # deque(['Mumbai', 'London', 'Berlin', 'Paris', 'Madrid', 'Rome'])
cities_list.popleft()
print(cities_list)      # deque(['London', 'Berlin', 'Paris', 'Madrid', 'Rome'])
cities_list.append('Bangalore')                 
print(cities_list)      # deque(['London', 'Berlin', 'Paris', 'Madrid', 'Rome', 'Bangalore'])
cities_list.extendleft(['Montreal','Toronto']) 
print(cities_list)      # deque(['Toronto', 'Montreal', 'London', 'Berlin', 'Paris', 'Madrid', 'Rome', 'Bangalore'])

# initializing new deque
de = collections.deque([1, 2, 3, 3, 4, 2, 4])
  
# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
# The first argument 4 is the element you're searching for.
# The second argument 2 is the optional start index. The search for the element will begin from this index.
# The third argument 5 is the optional end index. The search will end at this index (not inclusive).
print (de.index(4,2,5))     # 4
  
# using insert() to insert the value 3 at 5th position
de.insert(4,3)          
  
# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print (de)                  # deque([1, 2, 3, 3, 3, 4, 2, 4])
  
# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print (de.count(3))         # 3
  
# using remove() to remove the first occurrence of 3
de.remove(3)                
  
# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print (de)                  # deque([1, 2, 3, 3, 4, 2, 4])

# using extend() to add numbers to right end 
# adds 4,5,6 to right end
de.extend([4,5,6])
  
# printing modified deque
print ("The deque after extending deque at end is : ")
print (de)                  # deque([1, 2, 3, 3, 4, 2, 4, 4, 5, 6])
  
# using extendleft() to add numbers to left end 
# adds 7,8,9 to left end
de.extendleft([7,8,9])
  
# printing modified deque
print ("The deque after extending deque at beginning is : ")
print (de)                  # deque([9, 8, 7, 1, 2, 3, 3, 4, 2, 4, 4, 5, 6])
  
# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)
  
# printing modified deque
print ("The deque after rotating deque is : ")
print (de)                  # deque([1, 2, 3, 3, 4, 2, 4, 4, 5, 6, 9, 8, 7])        
  
# using reverse() to reverse the deque
de.reverse()
  
# printing modified deque
print ("The deque after reversing deque is : ")
print (de)                  # deque([7, 8, 9, 6, 5, 4, 4, 2, 4, 3, 3, 2, 1])

################################################################################################
# Counter class is a special type of object data-set provided with the collections module in Python3. Collections module provides the user with specialized container datatypes, thus, providing an alternative to Python’s general-purpose built-ins like dictionaries, lists, and tuples. 

#Counter is a sub-class that is used to count hashable objects. It implicitly creates a hash table of an iterable when invoked.

# elements() is one of the functions of Counter class, when invoked on the Counter object will return an itertool of all the known elements in the Counter object.

my_list = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
my_counter = Counter(my_list)
print(my_counter)               # Counter({5: 4, 2: 3, 1: 2, 3: 2, 6: 2, 7: 2, 4: 1})

sentence = "You are the great and you are the champ"
my_counter = Counter(sentence.split())
print(type(my_counter))         # <class 'collections.Counter'>
print(my_counter)               # Counter({'are': 2, 'the': 2, 'You': 1, 'great': 1, 'and': 1, 'you': 1, 'champ': 1})

series = [1,3,1,1,3,4,1,1,1,3,3,3,3,4,4,2,2,2,2,2,22,1,1]
lis1 = Counter(series)
print(lis1.most_common())       # [(1, 8), (3, 6), (2, 5), (4, 3), (22, 1)]

# gives first common element
print(lis1.most_common(1))      # [(1, 8)]

# gives first 3 common element
print(lis1.most_common(3))      # [(1, 8), (3, 6), (2, 5)]

################################################################################################
# Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the dictionary class that returns a dictionary-like object. The functionality of both dictionaries and defaultdict are almost same except for the fact that defaultdict never raises a KeyError. It provides a default value for the key that does not exists.

# Function to return a default
# values for keys that is not
# present
def def_value():
    return "Not Present"
      
# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2
  
print(d["a"])           # 1
print(d["b"])           # 2
print(d["c"])           # Not Present


# Defining the dict and passing 
# lambda as default_factory argument
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2
  
print(d["a"])           # 1
print(d["b"])           # 2
print(d["c"])           # Not Present

################################################################################################
# A namedtuple is a subclass of a regular tuple. It allows you to give names to each position in the tuple, making your code more readable and self-documenting. It's a lightweight alternative to defining a full class when you just need a simple data container.

# Define a namedtuple called 'Person' with fields 'name', 'age', and 'gender'
Person = collections.namedtuple('Person', ['name', 'age', 'gender'])

# Create instances of the namedtuple
person1 = Person(name='Alice', age=30, gender='Female')
person2 = Person(name='Bob', age=25, gender='Male')

# Access namedtuple fields using dot notation
print(person1.name)         # Alice
print(person2.age)          # 25

# Convert namedtuple to a dictionary
person_dict = person1._asdict()
print(person_dict)          # {'name': 'Alice', 'age': 30, 'gender': 'Female'}
