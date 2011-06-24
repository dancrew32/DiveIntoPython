#maps
li = [1, 9, 8, 4]
print [elem * 2 for elem in li] # [2, 18, 16, 8] .... badass
print li # [1, 9, 8, 4]


#keys, values, items
paramage = {'a':'dude', 'b':'no wai', 'c':'neato'}
paramage.keys() # ['a','b','c']
paramage.values() # ['dude','no wai', 'neato']
paramage.items() # [('a','dude'), ('b','no wai'), ('c','neato')]
# a list of key:val tuples! 
# let us map thisss!

print ['%s=%s' % (key, value) for key, value in paramage.items()]
# ['a=dude', 'b=no wai', 'c=neato']
