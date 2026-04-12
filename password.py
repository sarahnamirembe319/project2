import random
numbers="0123456789"
letters="abcdefghijklmnopqrstuvwxyz"
specials="!@#$%^&*()"

chars=letters+numbers+specials
print("your password generating......")
password=""
length=int(input("enter the length  of the password\n"))
for x in range(length):
	password+=random.choice(chars)
	
print(password)
 