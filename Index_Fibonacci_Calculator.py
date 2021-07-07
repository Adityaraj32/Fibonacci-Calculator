def getfibo(n):
    while True:
        if n == 1:
            return 0
        elif n== 2:
            return 1
        else:
            return getfibo(n-1) + getfibo(n-2)

var1 = int(input("enter an number: "))
print(getfibo(var1))