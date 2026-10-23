# This program counts how many numbers are entered by the user until they enter 0
count = 0
# Loop to read numbers until 0 is entered
while True:
    n = int(input("Enter a number:"))

    if n == 0:
        break

    count += 1

print(count)
