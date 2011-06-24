#getattr like a deathadder
li = ['larry', 'curly']
getattr(li, 'append')('dude') # the return value of getattr() IS the method
print li # ['larry', 'curly', 'dude']

#so basically you can build a list of methods you want to call,
# build a list of objects (or in this case, modules), then loop through
# and getattr(object, method) for each. you'll need to use type testing though

#type(getattr(object, method)) == types.FunctionType # True

# or by making sure it is something callable

#callable(getattr(object, method)) # True

#getattr takes a 3rd arg as the default arg, so you can do None testing
