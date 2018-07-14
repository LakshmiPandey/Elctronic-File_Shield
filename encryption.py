## importing the libraries
import os
import random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

## function to encrypt the given data
def encrypt(key, filedir, filename):
   outputFile = filedir+"/"+"(encrypted)"+filename
   filename = filedir+"/"+filename
   chunksize = 64*1024
   filesize = str(os.path.getsize(filename)).zfill(16)
   IV = ''
   for i in range(16):
       IV += chr(random.randint(0, 0xFF))
   encryptor = AES.new(key, AES.MODE_CBC, IV)
   with open(filename, 'rb') as infile:
     with open(outputFile, 'wb') as outfile:
          outfile.write(filesize)
          outfile.write(IV)
          while True:
              chunk = infile.read(chunksize)
              if len(chunk) == 0:
                  break
              elif len(chunk) % 16 != 0:
                   chunk += ' ' * (16 - (len(chunk) % 16))
              outfile.write(encryptor.encrypt(chunk))

## function to decrypt the given data
def decrypt(key, filedir,  filename):
    chunksize = 64*1024
    outputFile = filedir+"/"+filename
    filename = filedir+"/"+"(encrypted)"+filename
    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16) 
        
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(outputFile, 'wb') as outfile:
           while(True):
               chunk = infile.read(chunksize)
               if(len(chunk)) == 0:
                  break
               outfile.write(decryptor.decrypt(chunk))
           outfile.truncate(filesize)          
           
def getkey(passward):
    hasher = SHA256.new(passward)
    return hasher.digest() 