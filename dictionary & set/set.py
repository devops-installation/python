# set is a immutable
# set is unordered
# set is unindexed
# set is unchangeable
# set is unhashable
# l=[] #empty list
# print(type(l))
# t=() # empty tuple
# print(t)
# print(type(t))
# d={} #empty dict
# print(d)
# s=set() # empty set
# print(s)
# s={1,2,3,4} #set - no key:value
# print(type(s))
# print(s)
# n={1,2,3,1,2,3,4,5,5,6} # in set elemnt not repeate

# n.add('herry') #add {1, 2, 3, 4, 5, 6, 'herry'}
# print(n)
# print(len(n))
fruit={"apple", "orange" }
print(type(fruit), fruit)
fruit.update(["mango", 'grep']) #add multiple elemnt {'apple', 'grep', 'mango', 'orange'}
fruit.remove("apple") # remove "apple" {'mango', 'grep', 'orange'}
fruit.discard("ef") # Removing an element (does not raise an error if element is not found)
print(fruit)
fruit.clear()
print(fruit)

