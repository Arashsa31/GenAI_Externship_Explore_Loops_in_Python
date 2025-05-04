#Task 1 - Counting Down with Loops
countdown_number = int(input("Please provide a starting number for countdown: "))
while countdown_number > 0:
    print(countdown_number, end=" ") 
    countdown_number-=1
print("Blast off!\n")

#Task 2 - Multiplication Table with for Loops
multiplication_number = int(input("Please provide a number for the multiplication table(from 1 to 10): "))
min = 1
max = 11
for i in range (min, max):
    print(multiplication_number, " x ", i, " = ", multiplication_number*i)
print("")

#Task 3 - Find the Factorial
factorial_number = int(input("Please provide a Factorial number: "))
result = factorial_number
for i in range(1, factorial_number):
    result *= i
print("The factorial of ", factorial_number, " is ", result, end=".")