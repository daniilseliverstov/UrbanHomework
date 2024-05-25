numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
def f(n):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
    return is_prime
for n in numbers[1:]:
    if f(n) == False:
        not_primes.append(n)
    else:
        primes.append(n)

print('primes numbers: ',primes)
print('not primes numbers: ',not_primes)















