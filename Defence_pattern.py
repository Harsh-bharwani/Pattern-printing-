
n=int(input())
for i in range(n):
    for j in range(n):
        if(j==i):
            print("\\",end="")
        elif(i+j==7):
            print("/",end="")
        else:
            print("*",end="")
    print()    