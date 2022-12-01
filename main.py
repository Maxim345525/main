import random
try:
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

dict = (lambda lst: lst[::-1])
print(dict)