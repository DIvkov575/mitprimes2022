
def blind_signature(m, r, e, d, n):
    answer = pow(m*(r**e), d, n)

    return answer

print(blind_signature(25, 15, 25, 15, 40))
