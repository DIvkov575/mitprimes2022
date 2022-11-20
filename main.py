def part1(p, q, e):

    def EEA(k, m):
        prev_coefficient, coefficient_a = 1, 0
        prev_coefficient_b, coefficient_b = 0, 1
        while (m != 0):
            q = k // m  # find number of mod that can 'fit' within provided number
            k, m = m, k - q*m # finds remainder part of mod operation
            prev_coefficient_b, coefficient_b = coefficient_b, prev_coefficient_b - q*coefficient_b

        return prev_coefficient, prev_coefficient*k

        
    d, coeff_low = EEA(e, (p-1)*(q-1))

    if coeff_low != 1:
        print("ValueError: phi(n) and encryption-exponent passed are not coprime")
        return
    
    

    print(f"public (n, e): {p*q}, {e}")
    print(f"private (p, q, d): {p}, {q}, {d}")

