import random
start = int(input("start->"))
finish = int(input("finish->"))
size = int(input("size->"))
list = []

for i in range(size):
    list.append(random.randint(start, finish))

list.sort()
for item in list:
    print(item, end=" ")
print()

data = {1: lambda lst: max(lst), 2: lambda lst: min(lst)}
print(data[1](list))
print(data[2](list))