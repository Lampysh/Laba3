# This program counts how many numbers entered by the user are greater than the previous number until they enter 0
count = 0
prev = int(input("Enter the first number: "))
# Loop to read numbers until 0 is entered
while True:
    n = int(input("Enter a number: "))

    if n == 0:
        break

    if n > prev:
        count += 1

    prev = n

print(count)
