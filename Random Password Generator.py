import random

#A function to shuffle all the characters of a string
def shuffle(string):
 """
This code generates random passwords from upper and lowercase letters, numbers and special \
characters. Using the ASCII table the letters and punctuation are generated through ASCII code.
The output will always be different due to the random and shuffle modules

 """
 tempList = list(string)
 random.shuffle(tempList)
 return ''.join(tempList)

#Main program starts here
uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter (based on ASCII code)

lowercaseLetter1=chr(random.randint(97,122)) # Generate a random lower case letter (ASCII code)
lowercaseLetter2=chr(random.randint(97,122)) # Generate a second random lowercase letter (ASCII code)

digit1=(str(random.randint(0,9))) # generates a random digit between 0-9
digit2=(str(random.randint(0,9))) # generates a second random digit between 0-9

punctuationSign1=chr(random.randint(33,42)) # generates a random special character (ASCII)
punctuationSign2=chr(random.randint(64,94)) #generates a second special character (different to the first set)


#Generate a password using all of the characters, in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 \
+ digit1 + digit2 + punctuationSign1 + punctuationSign2

password = shuffle(password)

#Output
print(password)