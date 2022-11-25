import random

def signature_validation(m, d, n, e):
    def blind_signature(m, e, n):
        r = random.randint(1, n//m)
        return m*(r**e), r
    def extract_signature(m, d, n):
        return pow(m, d, n)
    
    b_sig, r = blind_signature(m, e, n)
    blind_signature = extract_signature(m, d, n)
    signature = blind_signature/r

signature_validation(25, 317, 437, 5)
