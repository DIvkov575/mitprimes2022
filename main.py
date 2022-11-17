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
    a = 253
    k = 3425
    m = 250
    b = 1 
    start = time.time()
    a %= m
    for _ in range(k):
        b = (b * a)%m
    print(b)
    print(time.time() - start)
    

    a = 253
    k = 3425
    m = 250
    b = 1

    a %= m
    start2 = time.time()
   
    def recurse(a,b,k):
        if float(k) <= 0:
            return b%m
        if k%2==0:
            k /= 2
            a **=2
            a %=m
            b = (b*a)%m
            return recurse(a,b,k)
        if k%2==1:
            return (a * recurse(a,b,k-1))%m
    b = recurse(a,b,k)
    print(b)
    print(time.time() - start2)

# 0.08165407




arbitrary()
