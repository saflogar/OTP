import binascii
import sys
import os
import random
import string
import getopt
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
    #print 'message='+message
    #print 'key='+key
    #cipherText = ''
    #for a,b in zip(key,message):
    #   print 'a='+a+'b='+b
    #  v=(ord(a) ^ ord(b))%27
    # cipherText = cipherText + chr(v)
    #print 'cipher='+ cipherText
    return "".join(chr(ord(a)^ord(b)) for a,b in zip (key,message))
       # print v
       # print 'des message:'+chr((v ^ ord(b)))
    
    

def main(argv):
    print 'Number of arguments:', len(sys.argv), 'arguments.'
    print 'Argument List:', str(sys.argv)
    try:
        opts, args = getopt.getopt(argv,"he:k:",["encrypt=","genKey="])
    except getopt.GetoptError:
        print 'otp -e <encrypt> -k <genKey>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'otp -e <encrypt> -k <generatekey>'
            sys.exit()
        elif opt in ("-e", "--encrypt"):
            print 'encrypt'
            #           inputfile = arg
        elif opt in ("-k", "--key"):
            print 'generate key'
      #          outputfile = arg
   #print 'Input file is "', inputfile
   #print 'Output file is "', outputfile
    #padLength= argv[1]
    #numKey = argv[2]
#    genRandom(padLength,numKey)
   # print cipher(cipher('hola'))
if __name__ == "__main__":main(sys.argv[1:])# with if
