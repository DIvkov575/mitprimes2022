def encrypt(n, e, m):
    c = (m**e)%n
    return c

def decryption(p, q, d, c):
    def binary_expo(a, b, n):
        if b <= 1:
            return a%n

        if b%2 == 0:
            tmp = binary_expo(a, b/2, n)
            return (tmp**2)%n

        if b%2 == 1:
            tmp = binary_expo(a, (b-1)/2, n)
            return (tmp**2 * a)%n

    # binary_expo(c, d, p*q)
    answer = binary_expo(295, 317, 437)
    return answer

