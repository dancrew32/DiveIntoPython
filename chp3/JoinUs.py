# le Join (strings only)
lol = {'lol':'wut', 'zomg':'nowai'}
joined = ';'.join(['%s=%s' % (key, value) for key, value in lol.items()])
print joined # lol=wut;zomg=nowai

# le split
print joined.split(';') # ['lol=wut', 'zomg=nowai']
print joined.split(';', 1) # number of times to split (1) optional argument


