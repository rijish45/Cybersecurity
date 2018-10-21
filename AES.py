#Rijish Ganguly
#rg239
#Tutorials to get acquainted with the library - https://www.youtube.com/watch?v=fqjdXMu4ZAQ



import os, random
import filecmp
import sys
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def encrypt(key, inputfilename, outputfilename):
	
	try:
		f = open(inputfilename, "r")
	except FileNotFoundError:
		printf("Input File doesn't exist")
		exit(1)

	try:
		f = open(outputfilename, "w")
	except FileNotFoundError:
		printf("Output File doesn't exist")
		exit(1)
	
	chunksize = 64 * 1024
	outputFile = outputfilename
	filesize = str(os.path.getsize(inputfilename)).zfill(16)
	IV = ''

	for i in range(16):
		IV += chr(random.randint(0, 0xFF))
	
	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(inputfilename, 'rb') as infile:
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


def decrypt(key, inputfilename, outputfilename):
	
	chunksize = 64*1024
	outputFile = outputfilename

	try:
		f = open(inputfilename, "r")
	except FileNotFoundError:
		print("Input File doesn't exist")
		exit(1)


	try:
		f = open(outputfilename, "w")
	except FileNotFoundError:
		print("Output File doesn't exist")
		exit(1)


	
	with open(inputfilename, 'rb') as infile:
		filesize = long(infile.read(16))
		IV = infile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)
        
      
        
		with open(outputFile, 'wb') as outfile:
			while True:
				chunk = infile.read(chunksize)

				if len(chunk) == 0:
					break

				outfile.write(decryptor.decrypt(chunk))
			outfile.truncate(filesize)


def GenerateKey(password):
	hashed = SHA256.new(password)
	return hashed.digest()

def Main():

         

        if(len(sys.argv) == 1):
		print("Syntax:\n" +
			"To encrypt:  ./AES -e <input_file> <output_file>\n" +
            "To decrypt:  ./AES -d <input_file> <output_file>\n")
	 
	crypt_type = sys.argv[1];

	if crypt_type == '-e':
		password = raw_input("Kindly enter the password: ")
		genpassword = GenerateKey(password)
		encrypt(genpassword, sys.argv[2], sys.argv[3])
		exit(0)
		
	elif crypt_type == '-d':
		password = raw_input("Kindly enter the password: ")
		genpassword = GenerateKey(password)
		decrypt(genpassword, sys.argv[2], sys.argv[3])
            
                
                
		exit(0)
	else:
		print("Wrong command or input style")
		exit(1)

if __name__ == '__main__':
	Main()
