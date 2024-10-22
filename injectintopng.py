# in bytes
end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

# open target file with appned bytes mode as f 
# then open exe that you want to inject with read bytes mode as e
with open('halloweencat.png', 'ab') as f, open('procexp64.exe', 'rb') as e:
	#we write whatever we read from e
	f.write(e.read())