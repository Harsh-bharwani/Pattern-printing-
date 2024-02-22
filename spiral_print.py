m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
r=4
c=4
jump=0
i=0
j=0
count=1
while(jump<c): #L to R
    m[i][j]=count
    jump+=1
    count+=1
    j=j+1
j-=1
i+=1
jump=0
r-=1
while(jump<r): #T to B
     m[i][j]=count
     jump+=1
     count+=1
     i=i+1
jump=0
i=i-1
c-=1
j=j-1
while(jump<c):  #R to L
    m[i][j]=count
    jump+=1
    count+=1
    j=j-1
j+=1
i-=1
jump=0
r-=1
while(jump<r):  #B to T
       m[i][j]=count
       jump+=1
       count+=1
       i=i-1
jump=0
i=i+1
c-=1
j=j+1
while(jump<c):  #L to R
    m[i][j]=count
    jump+=1
    count+=1
    j=j+1
j-=1
i+=1
jump=0
r-=1
while(jump<r):  #T to B
     m[i][j]=count
     jump+=1
     count+=1
     i=i+1
jump=0
i=i-1
c-=1
j=j-1
while(jump<c):  #R to L
    m[i][j]=count
    jump+=1
    count+=1
    j=j-1
j+=1
i-=1
jump=0
r-=1

for i in range(4):
    print(m[i])