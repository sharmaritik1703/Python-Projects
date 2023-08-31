__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

print("Welcome to Temperature Converter")
print("Enter 1 to convert F -> C and 2 to convert C -> F")

prompt = int(input("Enter the number (1/2): "))

if prompt == 1:
    temp1: float = int(input("Enter the temperature in F: "))
    temp2: float = (9/5 * temp1) + 32
    print(f"Temperature in Celcius: {temp2}")

elif prompt == 2:
    temp3: float = int(input("Enter the temperature in C: "))
    temp4: float = 5 / 9 * (temp3 - 32)
    print(f"Temperature in F: {temp4}")
