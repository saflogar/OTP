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
    
def cipher(numMess):
    keyfile = open ('keys','r')
    messageFile = open('messages','wb')
    j=0
    while j < int(numMess):
        message = raw_input('Enter message'+str(j+1)+':')
        key = keyfile.readline()
        
        messageFile.write(xorC(message,key)+'\n')
        j+=1
        print message
    messageFile.close()
    keyfile.close()
    
def decipher(num):
    keyfile = open('keys','r')
    keyFileLines = keyfile.readlines()
    keyfile.close()
    
    messageFile = open('messages','r')
    messageFileLines = messageFile.readlines()
    messageFile.close()

    cMessage = messageFileLines[int(num)]
    key = keyFileLines[int(num)]
    message = xorC(key,cMessage)
    
    messageFile = open('messages','w')
    keyfile = open('keys','w')
    
    j = 0
    for line in messageFileLines:
        if (j) != num:
            messageFile.write(line)
        j += 1
    
    j = 0
    for line in keyFileLines:
        if (j) != num:
            keyfile.write(line)
        j += 1

    print message

def main(argv):
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
    try:
        opts, args = getopt.getopt(argv,"he:k:d:",["encrypt=","genKey=","decrypt"])
    except getopt.GetoptError:
        print '-k <lenght> <# of keys> -e <# of messages> -d <index of message>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '-k <lenght> <# of keys> -e <# of messages> -d <index of message>'
            sys.exit()
        elif opt in ("-d","--decrypt"):
            num =int(arg)-1
            decipher(num)
        elif opt in ("-e", "--encrypt"):
            print 'encrypt'
            numMess = arg 
            cipher(numMess)
    #       inputfile = arg
        elif opt in ("-k", "--genKey"):
            padLength = arg
            numKeys = argv[2]
            print 'generate key'
            print 'padlength='+padLength+'numkeys='+numKeys
            genRandom(padLength,numKeys)
if __name__ == "__main__":main(sys.argv[1:])# with if
