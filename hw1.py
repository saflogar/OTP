import binascii
import sys
import os
import random
import string
import getopt
#print 'Number of arguments:', len(sys.argv), 'arguments.'
##print 'Argument List:', str(sys.argv)

def genRandom (padLength,numKey):
    keyfile = open('keys','wb')
    i = 0
    print numKey
    while i < int(numKey):
        key=''
        for j in range(0,int(padLength)):
            key = key + random.choice(string.ascii_letters)
        keyfile.write(key+'\n')
        print "ord"+ key
        i+=1
        print 'i:',i
    keyfile.close()

def xorC (m,k):
    #we use the same method for encription and decription of the message
    return "".join(chr(ord(a)^ord(b)) for a,b in zip (k,m))
    
def cipher(message):
    keyfile = open ('keys','r')
    key = keyfile.readline()
    messageFile = open('messages','a')
    messageFile.write(xorC(key,message)+'\n')
    messageFile.close()   
    
def decipher():
    keyfile = open('keys','r')
    key = keyfile.readline()
    messageFile = open('messages','r')
    cMessage = messageFile.readline()
    message = xorC(key,cMessage)
    
    print message

def main(argv):
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    try:
        opts, args = getopt.getopt(argv,"he:k:d",["encrypt=","genKey="])
    except getopt.GetoptError:
        print 'otp -e <encrypt> -k <genKey>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'otp -e <encrypt> -k <generatekey>'
            sys.exit()
        elif opt == '-d':
            decipher()
        elif opt in ("-e", "--encrypt"):
            print 'encrypt'
            message = arg 
            cipher(message)
    #       inputfile = arg
        elif opt in ("-k", "--key"):
            padLength = arg
            numKeys = argv[2]
            print 'generate key'
            print 'padlength='+padLength+'numkeys='+numKeys
            genRandom(padLength,numKeys)
if __name__ == "__main__":main(sys.argv[1:])# with if
