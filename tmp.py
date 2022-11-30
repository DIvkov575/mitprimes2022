with open("to_sign.txt", "r") as file:
    a = file.readlines()[1:2]
    b = a[0]
    print(b)
