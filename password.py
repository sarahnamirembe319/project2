import random
import string 

length = int(input("enter password length:"))

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
password = "join(random.choice(chars) for_in range(length))
	
print(password)
 
