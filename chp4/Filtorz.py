
# list filtering
li = ['a', 'b', 'c', 'd', 'e', 'farrrr', 'g', 'h', 'i', 'i']
print [el for el in li if len(el) > 1] # ['farrrr'], length filter
print [el for el in li if el != 'b'] # everything but 'b'
print [el for el in li if li.count(el) == 1] # everything but the two i's
    

