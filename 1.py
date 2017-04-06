import functutills
l = [1, 2, 3, 4]
def raise_2(number):
    return number **2

l2 = list(map(raise_2, l))
raise_2:lambda x: x**2

l = [1, 2, 3, 4]
l3 = list(map(lambda x: x**2, l))
print(l3)

# filter
# map
# reduce
# receive a lambda Function, returns a list
l = [1, 2, 3, 4]
l2 = list(filter(lambda x: x % 2 == 0, l))
print(l2)
s = int(reduce(lambda x,y: x + y, l))
print(s)
