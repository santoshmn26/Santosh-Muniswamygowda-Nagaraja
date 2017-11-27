def solution(s):
    c,res=0,list()
    for i in range(0,len(s),2):
        if(i+1<len(s)):
            res.append(s[i:i+2])
            continue
        res.append(s[i]+"_")
    return  (res)
print(solution("ab"))



