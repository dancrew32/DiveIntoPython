import odbchelper
import fib

dbHelperName = odbchelper.__name__
fibName = fib.__name__

# print built in object names
print dbHelperName + ' ' + fibName

# Dictionary (create, update, delete, append, prepend
d = {"a":"thing", "b":"other thing", "c": "final thing"}
print d["a"] # thing
print d["b"] # other thing

d["a"] = "new thing"
print d["a"] # new thing
del d["a"]
#print d["a"] #error
d.clear()
print d # {}


# Lists
li = ["a", "b", "dan", "z", "example"]
print li[0] # a
print li[4] # example
print li[1:3] # ['b', 'dan'] # a slice, starts at x [x:y] goes to y, but doesn't include y 
print li[:3] # take up to 3, so ['a', 'b', 'dan']
print li[3:] # take after 3, so ['z', 'example']
print li[:] #makes a complete copy of the list
li.append('cheese')
print li[5] # cheese
li.insert(2, 'cow')
print li[2] # cow
li.extend(['dog', 'bird'])
print li[7:] # ['dog', 'bird']
print li.index('dog') # 7
print 'c' in li # False
li.remove('z')
'z' in li # False
print li.pop() # bird (removed from li and returned)

nli = ['a', 'b']
nli = nli + ['c', 'd']
print nli # ['a', 'b', 'c', 'd']
nli += ['e'] # appends e
tuple(nli) #freeze list

# True and False
# 0 is false, all other numbers are true
# "" is false, other strings are true
# [] is false, other lists are true
# () is false, other tuples are true
# {} is false, other dictionaries are true


# Tuples
# Tuples are immutable lists (Read only once created)
t = ('a', 'b', 'c');
print t[0] # a
print t[0:] # ('b', 'c') (slicing works, when you slice, you get a new tuple)
#tuple's have no other methods
print 'c' in t # True
list(t) #thaw tuple
