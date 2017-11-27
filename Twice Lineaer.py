def dbl_linear(n):
    a,c=[1],0
    for i in a:
        if (2*i)+1 not in a:
            a.append((2*i)+1)
        if (3*i)+1 not in a:
            a.append((3*i)+1)
        c+=1
        a.sort()
        if(len(a)>=2*n):
            break
    print(a)
    return(a[n])
print(dbl_linear(6000))