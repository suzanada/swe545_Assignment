import xmlrpclib

client = xmlrpclib.ServerProxy('http://localhost:8000/')
sNumber = client.randomNumberGenerator()
print "Please guess a number between 0 and 100"


while True:
    try:
        cNumber = int(raw_input("What is your guess?"))
        print client.comparison(sNumber, cNumber)
        if cNumber == sNumber:
            break
    except:
        print("Please enter a valid number from 0 to 100")




