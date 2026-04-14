def rev(n,r=0):
    if len(n)==0:
        return r
    else:
        d=n%10
        r=r*10+d
        return rev(n//10,rev)
num = int(input("Enter a number: "))
print(f"Reversed number: {rev}")
