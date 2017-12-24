def is_valid_IP(strng):
    s=strng.split(".")
    f=None
    if((len(s)==4)):
        for i in s:
            if(i=="0"):
                f=True
                break
            if(i.isdigit())&(i[0]!="0"):
                if((int(i)<=255)&(int(i)>=0)):
                    f = True
                else:
                    f = False
                    break
            else:
                f = False
                break
    else:
        return(False)
    return(f)

print(is_valid_IP("127.1.1.0"))
