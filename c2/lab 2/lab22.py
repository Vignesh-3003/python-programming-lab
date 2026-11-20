number = int(input("Enter a number: "))

# Prime Number Checking

if number > 1:

    for i in range(2, number):

        if number % i == 0:
            print(number, "is not a prime number")
            break

    else:
        print(number, "is a prime number")

else:
    print(number, "is not a prime number")


# Factorial Calculation

factorial = 1

for i in range(1, number + 1):
    factorial = factorial * i

print("Factorial:", factorial)