def countBits(n):
    rem=list()
    while(n>=1):
        rem.append(n%2)
        n = n//2
    rem.reverse()
    sol=rem.count(1)
    print(rem,sol)
countBits(1234)

