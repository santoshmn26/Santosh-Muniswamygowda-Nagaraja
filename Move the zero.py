def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
move_zeros([False,'a',1,0,2,3,True,0,2,3,0,94,0,1,2])