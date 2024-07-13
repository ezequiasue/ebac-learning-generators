# Traditional way
X = [1, 2, 3, 4, 5]
for i in X:
    print(i)

print("#########################################################")
# Same thing, but different

x1 = [1, 2, 3, 4, 5]
y = iter(x1)
try:
    while True:
        print(next(y))
except StopIteration as e:
    pass
