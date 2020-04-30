a=int(input())
A = []

for i in range(0,a):
    A.append(int(input()))

for i in range(0,a):
    if i%2==0:
        print(A[i])
