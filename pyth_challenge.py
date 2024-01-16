import math
def isPrime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    upper_limit = int(math.sqrt(x)+1)
    for num in range(3,upper_limit,2):
        if x%num == 0:
            return False
    return True

open('NewPrimes.txt', 'w').close()
def check_for_primes(min,max):
    for num in range(min, max+1):
        if isPrime(num) == True:

            with open('NewPrimes.txt','a') as file:
                file.write(str(num))
                file.write('\n')

check_for_primes(1,250)


#print(isPrime(95))