from difflib import SequenceMatcher
class Dictionary:
    def __init__(self,words):
        self.words=words
        self.p,self.l1,self.l2=0,0,0
        self.dict1={}
    def find_most_similar(self,term):
        p=0
        for i in self.words:
            for j in term:
                l1=term.count(j)
                l2=i.count(j)
                if(l1==l2):
                    p=p+1
            #print(len(i),len(check))
            if((len(term)==len(i)-1)|(len(term)==len(i)+1)):
                p=p+1
            self.dict1[i]=p
            p=0
        #print(dict1)
        inverse = [(value, key) for key, value in self.dict1.items()]
        m,c=0,""
        for i in self.dict1:
            v=self.dict1[i]
            if(v>=m):
                m=v
                c=(i)
        print(c)
        print(self.dict1)

words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
test_dict=Dictionary(words)
while(True):
    x=input("---")
    test_dict.find_most_similar(x)