import string, random

randPass = ""
specialChar = "-|@.,?/!~#%^&*(){}[]\=*"

#random number between 6 and 24
randLength = int(random.randint(6,24)/4)

for i in range(randLength):
    #random chracters
    randPass += random.choice(string.ascii_lowercase)
    randPass += random.choice(string.ascii_uppercase)
    randPass += random.choice(string.digits)
    randPass += random.choice(specialChar)
    
#check to see if password length is below minimum
if randLength == 1:
    for i in range(2):
        randPass += random.choice(string.printable)

print("The Random Password is " + randPass)



