def circulate(c,n):
    for i in range(1,n+1):
        d=c[i:]+c[:i]
        print("circulate","=",d)
    return
c=[178,289,324,448,570,698,188,842,956,106]
n=int(input("enter n:"))
circulate (c,n)
