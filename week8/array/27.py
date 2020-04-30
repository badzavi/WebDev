a=int(input())
A=[]
c=0
for i in range(0,a):
    A.append(int(input()))

for i in range(0,a):
    if A[i]>=0:
        c=c+1

print(c)        