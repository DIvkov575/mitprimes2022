
def generateKeys(p, q, e):
    def eea(k, m):
        prev_coefficient, coefficient_a = 1, 0
        prev_coefficient_b, coefficient_b = 0, 1
        while (m != 0):
            q = k // m  # find number of mod that can 'fit' within provided number
            k, m = m, k - q*m # finds remainder part of mod operation
            prev_coefficient_b, coefficient_b = coefficient_b, prev_coefficient_b - q*coefficient_b

        return prev_coefficient, prev_coefficient*k

        
    d, coeff_low = eea(e, (p-1)*(q-1))

    if coeff_low != 1:
        print("ValueError: phi(n) and encryption-exponent passed are not coprime")
        return
    
    print(f"public key n: {p*q}")
    print(f"private key d: {d}")


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

    answer = binary_expo(c, d, p*q)
    return answer


def decryption_implemented():
    # part 4: implementing decryption for p = 8783, q = 9133, e = 5, m = 34367293
    p = 8783
    q = 9133
    e = 5
    m = 34367293

    def euclid_func(k, m):
        remainder = m  # rename for better readability
        prev_coefficient, coefficient_a = 1, 0
        prev_coefficient_b, coefficient_b = 0, 1

        while (remainder != 0):
            q = k // remainder  # find number of mod that can 'fit' within provided number
            k, remainder = remainder, k - q * remainder  # finds remainder part of mod operation

            prev_coefficient, coefficient_a = coefficient_a, prev_coefficient - q * coefficient_a
            prev_coefficient_b, coefficient_b = coefficient_b, prev_coefficient_b - q * coefficient_b

        return prev_coefficient

    d = euclid_func(e, (p-1)*(q-1))

    result = decryption(p, q, d, m)
    print(result)
