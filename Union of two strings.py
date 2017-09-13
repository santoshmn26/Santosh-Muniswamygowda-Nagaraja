def longest(s1, s2):
    s3=set.union(set(s1),set(s2))
    s=list()
    for i in s3:
        s.append(i)
        #print(s)
    s.sort()
    res=""
    for i in s:
        res=res+i
    return(res)
longest("aretheyhere", "yestheyarehere")