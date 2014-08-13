import binascii
import sys
import os
import random
import string
#print 'Number of arguments:', len(sys.argv), 'arguments.'
##print 'Argument List:', str(sys.argv)


def genRandom (padLength,numKey):
    file = open('keys','wb')
    i = 0
    print numKey
    while i < int(numKey):
        key=''
        for j in range(0,int(padLength)):
            key = key + random.choice(string.ascii_letters)
        file.write(key+'\n')
        print "ord"+ key
        i+=1
        print 'i:',i
    file.close()
        

def cipher(message):
    file = open ('keys','r')
    key=file.readline()
    #zip(key,message)
    print 'message='+message
    print 'key='+key
    cipherText = ''
    for a,b in zip(key,message):
        print 'a='+a+'b='+b
        v=(ord(a) ^ ord(b))%27
        cipherText = cipherText + chr(v)
    print 'cipher='+ cipherText
       # print v
       # print 'des message:'+chr((v ^ ord(b)))
    
    

def main(argv):
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    
    padLength= argv[1]
    numKey = argv[2]
#    genRandom(padLength,numKey)
    cipher('hola')
if __name__ == "__main__":main(sys.argv)# with if
