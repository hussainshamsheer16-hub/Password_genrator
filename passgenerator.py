import random
import string

length = int( input("Please Enter Length of Password: "))
chars = string.ascii_letters + string.digits + string.punctuation
generatedpass = ''.join(random.choice(chars) for _ in range(length))
print("Generated Password is ", generatedpass)