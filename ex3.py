
def calc(i,b):
    if i % b != 0:
        return 1
    else:
        return 0

foo = 10000
arr = []
for i in range(2, foo + 1, 2):
    if all([ calc(i,3), calc(i,5), calc(i,7) ]):
        arr.append(i)
print(len(arr))

