import xmlrpclib
from random import randint


server = xmlrpclib.Server("http://www.advogato.org/XMLRPC")

def randomNumberGenerator():
    return randint(0,100)

ranNum1 = randomNumberGenerator()
ranNum2 = randomNumberGenerator()

print "Random Number 1:",str(ranNum1)
print "Random Number 2:",str(ranNum2)


print "The sum of Random Number 1 and Random Number 2: ", server.test.sumprod(ranNum1,ranNum2)[0]
print "The product of Random Number 1 and Random Number 2: ", server.test.sumprod(ranNum1,ranNum2)[1]
