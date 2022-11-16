import time
a = 992
k = 9212343234
m = 1000


def arbitrary():
    # a = int(input("a: "))
    # k = int(input("k: "))
    # m = int(input("m: "))
  
    # if (a == m):
    #     return 0
    a = 126
    k = 1000000
    m = 250
    b = 1 
    start = time.time()
    
    a %= m


    for _ in range(k):
        b = (b * a)%m
    print(b)


    print(time.time() - start)





arbitrary()
