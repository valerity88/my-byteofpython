i = []
i.append('item')
print(repr(i))
if eval(repr(i)) == i:
    print(True)
