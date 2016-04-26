import xmlrpclib

client = xmlrpclib.ServerProxy('http://localhost:8000/')
sNumber = client.randomNumberGenerator()

cNumber = int(raw_input("What is your guess?"))
print sNumber
print client.comparison(sNumber,cNumber)
while client.comparison(sNumber,cNumber) != "You win, This is the number that was guessed":
    cNumber = int(raw_input("What is your guess?"))
    client = xmlrpclib.ServerProxy('http://localhost:8000/')
    print client.comparison(sNumber, cNumber)



