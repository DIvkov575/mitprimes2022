
n = 604*10**14
print(n)
d = 2.63856689*10**33
print(d)

a = 1

for i in range(n+1):
    a*= (d-i)/d
    print(n-i+1)

print(a)
