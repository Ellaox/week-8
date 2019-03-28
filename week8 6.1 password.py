#password.py
#Program prompts user to enter the password until they do so correctly.
#Written by P.K., January 24th 2005

print "Entry is password protected.",
password = raw_input("Enter the password! ")

while password != "python":
    print "Entry is password protected.",
    password = raw_input("Enter the password! ")

print "Welcome!"


#The only lines of code that are new in the above program are those that form the while lopp structure

while password != "python":
    print "Entry is password protected.",


#Syntax (general form of the while loop in Python)
        
