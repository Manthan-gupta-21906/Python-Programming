# defining the function to check prime number
def prime(n):
    is_prime = True
    for i in range(2, n):
        if n%i==0:
            is_prime = False
    if is_prime:
        print(f"given number {n} is a prime number")
    else:
        print(f"given number {n} is not a prime number")


n = int(input("Enter a number: "))

prime(n)