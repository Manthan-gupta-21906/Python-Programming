def armstrong_sum(n, digits):
    if n == 0:
        return 0
    else:
        n1 = n % 10
        return (n1 ** n1) + armstrong_sum(n // 10, digits)

num = int(input("Enter a number: "))
digits = len(str(num))

result = armstrong_sum(num, digits)

if result == num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")