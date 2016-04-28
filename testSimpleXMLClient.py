import xmlrpclib

client = xmlrpclib.ServerProxy('http://localhost:8000/')
print client.system.listMethods()
print client.add(3, 1 )
print client.subtract(5,2)
print client.system.methodHelp('subtract')