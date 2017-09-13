def pig_it(text):
    text1=text.split()
    c=0
    for i in text1:
        x=i[0]
        if (text1[c].isalpha()):
            text1[c]=text1[c]+x
            text1[c]=text1[c][1:]+"ay"
        c += 1
    t=""
    for i in text1:
        t=t+i + " "
    s=len(t)
    return(t[:(s-1):])
print(pig_it("Pig latin is cool"))