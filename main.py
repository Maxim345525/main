try:
    size = int(input("Введіть число:"))
    begin = -50
    end = 50
    my_text = []
    for j in range(size):
        my_text.append(random.randint(begin, end))




    random.shuffle(my_text)
    print(my_text)
    data = {1: lambda lst: max(lst), 2: lambda lst: min(lst)}
    print(data[1](my_text))
except Exception as ex:
    print(ex)


