#    lis = ["BMW", "MB", "LADA", "KIA", "HONDA"]
#    cars_count = 0
#    for i in lis:
#    print('я езжу на автомобиле марки', i)
#    cars_count += 10
#print(cars_count)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
pr = []
npr =[]

primes = [r for r in numbers if is_prime(r)]
not_primes = [r for r in numbers if not is_prime(r)]
print(primes)
print(not_primes)