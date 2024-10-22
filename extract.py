# in bytes
end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

# open the privously targeted file with read bytes mode as f
# Use offset to read from that point on
with open('halloweencat.png', 'rb') as f:
	content = f.read()
	offset = content.index(end_hex)
	f.seek(offset + len(end_hex))

#Open a new file to extract injected exe by using write bytes mode
	with open('evil.exe', 'wb') as e:
		e.write(f.read())