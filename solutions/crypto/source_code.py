import sys
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext,shift):
	cipher = ''
	plaintext = plaintext.upper()
	for i in range(0,len(plaintext)):
		each = plaintext[i]
		if each in alphabet:
			c = (ord(each)+shift+i-0x41) % 26 + 0x41
			cipher += chr(c)
		else:
			cipher += (each)
	return cipher

def menu():
	print ("[1] encrypt ")
	print ("[2] read source code")
	print ("[3] encrypted data")
	sys.stdout.flush()

if __name__ == "__main__":
	fIn = open("flag","r")
	menu()
	try:
		choise = raw_input("").strip()
	except (EOFError):
		sys.exit(0)

	if choise == "1":
		print ( "give me your data: " )
		sys.stdout.flush()
		try:
			inputData = raw_input("").strip()
			for i in range(0,26):
				print  "#",i, "\t=>\t", encrypt( inputData, i )
		except (EOFError):
			sys.exit(0)
	elif choise == "2":
		print ( "#" *40 )
		print ( open("Crypto.py", "r").read() )
		print ( "#" *40 )
	elif choise == "3":
		print ("LWIC{ZYDSBT_MX_WZXEO_BT_OFM}")
	else:
		print( "bad input" )
