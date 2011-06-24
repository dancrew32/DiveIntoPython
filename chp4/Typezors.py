#types
print type(1) #<type 'int'>
li = []
print type(li) #<type 'list'>
import apihelper
print type(apihelper) #<type 'module'>
import types
print type(apihelper) == types.ModuleType # True. types can be compared to types.*


#str(), literal string render
print str(1) #'1'
print apihelper # <module 'apihelper' from '/home/dan/www/DiveIntoPython/chp4/apihelper.pyc'>
print str(None) # 'None'
#note, None is python's null


#dir(), returns methods of a list
li = []
dir(li) # ['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']


#callable
import string
print string.punctuation # all of the punctuation
print string.join  #<function join at 00C55A7C>
callable(string.punctuation) #False, because strings don't have methods to call
callable(string.join) #True, because there are methods you can call


#built in functions
from apihelper import info
import __builtin__
info(__builtin__, 20) #epic length list of builtin methods

