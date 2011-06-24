k = 'uid'
v = 'sa'

"%s=%s" % (k, v) # evaluate expression to string
# this is a lot like C#'s String.format("{0}={1}", k, v)
# only (k, v) is a tuple

userCount = 6
print "Users Connected: %d" % (userCount, ) # kinda icky, but tuple's require at least one comma
#print 'users connected:' + userCount # throws exception

print "a nice float looks like %f" % 50.462500 # a nice float looks like 50.462500
print "a nice float looks like %.2f" % 50.462500 # a nice float looks like 50.46
print "a nice float looks like %+.2f" % 50.462500 # a nice float looks like +50.46

