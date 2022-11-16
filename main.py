def euclid_func(k, m):
    # a represents number the inverse
    """
        q variable represents 'number of mod that fit within current dividend'
        remainder represents remainder from division that occurs when creating 'q' listed in above line
        k represents dividend
        coefficient_a represents first coefficient of Bezout's Identity
        prev_coefficient represets coefficient_a from previous iteration
        coefficient_b represents second coefficient of Bezout's Identity
        prev_coefficient_b represets coefficient_b from previous iteration


    Args:
        k: represents number inverse is being taken of
        m: represents mod
    
    return:
        returns modular multiplicative inverse 
    """

    remainder = m  # rename for better readability
    prev_coefficient, coefficient_a = 1, 0
    prev_coefficient_b, coefficient_b = 0, 1

    while (remainder != 0):
        # find initial remainder/coefficient for 'standard' Euclidean Algorithm part of Extended Eulclidean Algorithm ie. finding gcd
        # finds mod of given numbers
        q = k // remainder  # find number of mod that can 'fit' within provided number
        k, remainder = remainder, k - q*remainder # finds remainder part of mod operation

        # 'extended' portion of EEA, updates coefficients of Bezout's Identity
        prev_coefficient, coefficient_a = coefficient_a, prev_coefficient - q*coefficient_a
        prev_coefficient_b, coefficient_b = coefficient_b, prev_coefficient_b - q*coefficient_b



    return prev_coefficient

a = euclid_func(7, 120)
# print("modular multiplicative inverse of 7 mod 120:", euclid_func(7, 120))
# print("modular multiplicative inverse of 100 mod 22391:", euclid_func(100, 22391))
# print("modular multiplicative inverse of 10799 mod 46994636:", euclid_func(10799, 46994636))







# def problem1_part1(a, b):
#     # Part 1    
#     # (10 + 9) % 13
#     # a = 10 + 9
#     # b = 13
#     i = 0
#     while abs(i) < 10:
#         if a > i*b:
#             if (i*b <= a) and ((i+1)*b > a):
#                 # print("answer", a - i*b)
#                 # print("answer", a % b)
#                 return (a - i*b)
#                 # break
#             else:
#                 i += 1
#         if a < i*b:  
#             if (i*b >= a) and ((i+1)*b < a):
#                 # print("answer", a - i*b)
#                 # print("answer", a % b)
#                 return (a - i*b)
#                 # break
#             else:
#                 i -= 1
# # part1
# problem1_part1(10+9, 13)
# problem1_part1(5-12, 13)
# problem1_part1(11*5, 13)
#
