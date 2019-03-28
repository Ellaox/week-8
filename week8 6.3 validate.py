#validate.py
#Program prompts user to enter an integer between 5 and 10 (inclusive) until
#they do so correctly.
#Written by P.K., January 24th 2005


number = input("Enter an integer that is odd and greater than 50: ")
aa = number % 2

while aa == 0.0 or number <=50:
    print "Invalid input!",
    number = input("Enter an integer that is odd and greater than 50: ")
    aa = number % 2


print "Thank you!"
