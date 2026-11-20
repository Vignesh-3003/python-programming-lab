print("UNIT CONVERTER")

print("1. Kilometres to Miles")
print("2. Miles to Kilometres")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

value = float(input("Enter value: "))

if choice == 1:
    result = value * 0.621371
    print("Miles:", round(result, 2))

elif choice == 2:
    result = value / 0.621371
    print("Kilometres:", round(result, 2))

elif choice == 3:
    result = (value * 9/5) + 32
    print("Fahrenheit:", round(result, 2))

elif choice == 4:
    result = (value - 32) * 5/9
    print("Celsius:", round(result, 2))

else:
    print("Invalid choice")