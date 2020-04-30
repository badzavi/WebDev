n =int(input())

i = 1

ch = False

while i <= n :
    if i == n :
        ch = True
    
    i *= 2

    if ch == True:
        print("YES")


if ch == False:
    print("NO")