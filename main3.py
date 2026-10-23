# Count the number of zeros entered by the user
n = int(input("Enter a number: "))
count = 0 
# Count the number of zeros
for i in range(n):
    x = int(input("Enter a number: "))
    if x ==0:
        count +=1
# Print the count of zeros
print(count)
