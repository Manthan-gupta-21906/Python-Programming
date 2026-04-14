def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)
    
def lcm(a, b):
    return (a * b) // hcf(a, b)

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(f"hcf : {hcf(n1,n2)}\nlcm : {lcm(n1,n2)}")
