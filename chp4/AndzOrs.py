# and
print 'a' and 'b' #b true so returns last value
print '' and 'b' #''  false so returns the first value
print 'a' and 'b' and 'c' #c, true, last value

#or, return first value that is true immediately
print 'a' or 'b' #a, a is true, so a first
print '' or 'b' #b b is first true, so b
print '' or [] or {} # {} if all are false, final returns

def leFunc:
    print 'in leFunc()'
    return 1
print 'a' or leFunc() # a first

#andor
yo = 'cool'
sup = 'breh'
print 1 and yo or sup #cool
print 0 and yo or sup #b
#this is test == true ? yo : sup; in C!!

#make sure empty strings are never falsy
gnar = ''
bean = 'salad'
1 and [gnar] or [bean]
