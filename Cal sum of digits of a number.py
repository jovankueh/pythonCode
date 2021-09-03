# Python program to find the sum of digits of a number using while loop of any integer number

print("Enter the integer number::\n")

x, sum, m = int(input()), 0, None

print ("The sum of ", x, " digits is = ", end= "")

while x > 0:
    m = x % 10
    m = int (m)
    sum = sum + m
    x = x / 10
    x = int (x)


print (sum, "\n")
