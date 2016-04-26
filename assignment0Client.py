import xmlrpclib

server = xmlrpclib.Server("http://www.advogato.org/XMLRPC")
i = server.test.guess()
server = xmlrpclib.Server("http://www.advogato.org/XMLRPC")
b = server.test.guess()
print "Random Number 1:",i[1]
print "Random Number 2:",b[1]
print "The sum of these 2 numbers is: ", server.test.sumprod(i[1],b[1])[0]
print "The product of these 2 numbers is: ", server.test.sumprod(i[1],b[1])[1]