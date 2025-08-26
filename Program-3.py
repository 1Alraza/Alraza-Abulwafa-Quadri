k=1
a=int(input("enter the number : "))
i=1
if a % 2 == 0:   
    n = a - 1
else:           
    n = a
while i<=n:
    if i==n:
        print(k)
        break
    print(k,end=", ")
    k=k+2
    i+=1