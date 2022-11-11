def problem1(a, b):
    # Part 1    
    # (10 + 9) % 13
    # a = 10 + 9
    # b = 13
    i = 0
    while abs(i) < 10:
        if a > i*b:
            if (i*b <= a) and ((i+1)*b > a):
                # print("answer", a - i*b)
                # print("answer", a % b)
                return (a - i*b)
                # break
            else:
                i += 1
        if a < i*b:  
            if (i*b >= a) and ((i+1)*b < a):
                # print("answer", a - i*b)
                # print("answer", a % b)
                return (a - i*b)
                # break
            else:
                i -= 1
# part1
problem1(10+9, 13)
problem1(5-12, 13)
problem1(11*5, 13)

