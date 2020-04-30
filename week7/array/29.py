a=int(input())
A=[]
ok=False
for i in range(0,a):
    A.append(int(input()))

for i in range(0,a):
     if A[i]==A[i-1]: 
         ok=True
         break
     

if ok: print('YES')
else: print('NO')
