def domain_name(url):
    print(url)
    x=len(url)
    c,s=0,None
    for i in range(x):
        if('/' not in url)&(s==None):
            url = url.replace("www.", "")
            s=0
            continue
        if (url[i]=='/')&(s==None):
            s=i+2
            if("www." in url):
               url= url.replace("www.","")
        if(s!=None):
            if(url[i]=='.')|(url=='/'):
                c=i
                break
    print(url[s:c])


    return(0)




domain_name("www.xakep.ru")