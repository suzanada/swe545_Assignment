import SimpleXMLRPCServer
import random

def randomNumberGenerator():
    return random.randint(0,100)

def comparison(sNumber,cNumber):
    if sNumber > cNumber:
        return "bigger than this"
    elif sNumber < cNumber:
        return "smaller than this"
    else:
        return "You win, This is the number that was guessed"


server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost",8000))
server.register_function(comparison)
server.register_function(randomNumberGenerator)
server.serve_forever()

