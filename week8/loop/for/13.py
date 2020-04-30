import math
a=int(input())
b=int(input())

for i in range(a,b+1):
   sqrt=int(math.sqrt(i))
   if(sqrt*sqrt==i):
       print(i)