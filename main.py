def count_primes(num):
    for n in range(2,num+1):
        prime=True
        for i in range(2,n):
            if(num%i == 0):
                prime=False
        if prime:
            print(n)