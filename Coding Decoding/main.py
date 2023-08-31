__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

import time
from random import randint

def encode(text: str, encode_amount: int) -> str:
    encoded_message: str = ""
    for character in text:
        shifted_value: int = ord(character) + encode_amount
        encoded_message += chr(shifted_value)

    return encoded_message

def decode(text: str, decode_amount: int) -> str:
    decoded_message = ""

    for element in text:
        shifted_value: int = ord(element) - decode_amount
        decoded_message += chr(shifted_value)

    return decoded_message

print("Welcome to Coding and Decoding Program")
time.sleep(0.1)

message = input("Enter you message: ")
time.sleep(0.1)

print("Do you want to specify the value for encode or decode? If yes enter the value otherwise type 0")
value = int(input("Enter the value: "))
time.sleep(0.1)

amount = value if value != 0 else randint(1, 10)
print(f"Your secret number is {amount}")
time.sleep(0.1)

prompt = input("Tell whether you want to encode or decode (E/D)? : ")

if prompt == "E":
    result = encode(text=message, encode_amount=amount)
    print(f"Encoded message is -> {result}")

elif prompt == "D":
    result = decode(text=message, decode_amount=amount)
    print(f"Decoded message is -> {result}")
