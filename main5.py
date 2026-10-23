# This program calculates the sum of the digits of a given integer number.
n = int(input("Enter a number: "))

n = abs(n)
s = 0
# Loop to calculate the sum of the digits
while n > 0:
    s += n % 10
    n //= 10

print(s)
