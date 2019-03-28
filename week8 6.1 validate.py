#validate.py
#Program prompts user to enter an integer between 5 and 10 (inclusive) until
#they do so correctly.
#Written by P.K., January 24th 2005


number = input("Enter an integer that is positive and less than 25: ")

while number <0 or number >25:
    print "Invalid input!",
    number = input("enter a positive number that is less than 25: ")

print "Thank you!"
