import random


symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
print("Glad you've arrived at our password creation tool.")
len_password = int(input("Password length: "))
password = ""

for i in range(len_password):
    password += random.choice(symbols)
print(password)
