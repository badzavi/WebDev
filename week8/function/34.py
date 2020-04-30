def Xor(x,y):
    if x!=y and (x==1 or y==1):
        return 1
    else:
        return 0

a=int(input())
b=int(input())

print(Xor(a,b))