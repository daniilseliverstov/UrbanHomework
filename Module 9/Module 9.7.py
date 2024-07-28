from math import sqrt


def is_prime(funk):
    def primus_est(*argumentis):
        i = 2
        exitum = funk(*argumentis)
        while i <= sqrt(exitum):
            if exitum % i == 0:
                print('Составное')
                break
            if exitum > 1:
                print('Простое')
                break
        return exitum
    return primus_est


@is_prime
def summa_valorum(*argumentis):
    totalis = 0
    for initium in argumentis:
        totalis += initium
    return totalis


result = summa_valorum(2, 3, 6, 6)
print(result)
