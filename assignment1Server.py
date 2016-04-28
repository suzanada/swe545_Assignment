import SimpleXMLRPCServer
import random


server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost",8000))
#exitGame= False

def randomNumberGenerator():
    return random.randint(0,100)

def comparison(sNumber,cNumber):
    #global exitGame=False
    if int(cNumber)<0 & int(cNumber)>100:
        return "Please enter a valid number between 0 and 100"
    else:
        if int(sNumber) > int(cNumber):
            return "You should guess a number bigger than this.."
        elif int(sNumber) < int(cNumber):
            return "You should guess a number smaller than this.."
        else:
            return "You win, This is the correct number"

            #exitGame=True

server.register_function(comparison)
server.register_function(randomNumberGenerator)
#if exitGame = False:
server.serve_forever()


