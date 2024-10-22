# malcat
png injection example

```
❯ ll
total 5736
drwxr-xr-x  10 l  s      320 Oct 22 13:14 .
drwxr-xr-x   3 l  s       96 Oct 22 12:47 ..
drwxr-xr-x  13 l  s      416 Oct 22 12:48 .git
-rw-r--r--   1 l  s       31 Oct 22 12:47 README.md
-rw-r--r--   1 l  s     3012 Oct 22 12:35 aboutPNG.txt
-rw-r--r--   1 l  s      423 Oct 22 12:10 extract.py
-rw-r--r--@  1 l  s   529444 Oct 22 10:42 halloweencatOG.png
-rw-r--r--   1 l  s      317 Oct 22 12:42 injectintopng.py
-rw-r--r--   1 l  s     1045 Oct 22 12:35 injectionWriteup.txt
-rw-r--r--@  1 l  s  2381232 Oct 22 11:19 procexp64.exe
❯ cp halloweencatOG.png halloweencat.png
```
Before you start check the 256 sha of procexp64.exe
```
❯ shasum -a 256 procexp64.exe
8158dc0569972c10056f507cf9e72f4946600ce163c4c659a610480585cd4935  procexp64.exe
```

```
❯ cat injectintopng.py
# in bytes
end_hex = b"\x00\x00\x00\x00\x49\x45\x4e\x44\xae\x42\x60\x82"

# open target file with appned bytes mode as f 
# then open exe that you want to inject with read bytes mode as e
with open('halloweencat.png', 'ab') as f, open('procexp64.exe', 'rb') as e:
	#we write whatever we read from e
	f.write(e.read())%
❯ python3 ./injectintopng.py
❯ ll
total 11424
drwxr-xr-x  11 l  s      352 Oct 22 13:14 .
drwxr-xr-x   3 l  s       96 Oct 22 12:47 ..
drwxr-xr-x  13 l  s     416 Oct 22 12:48 .git
-rw-r--r--   1 l  s       31 Oct 22 12:47 README.md
-rw-r--r--   1 l  s     3012 Oct 22 12:35 aboutPNG.txt
-rw-r--r--   1 l  s      423 Oct 22 12:10 extract.py
-rw-r--r--@  1 l  s  2910676 Oct 22 13:15 halloweencat.png
-rw-r--r--@  1 l  s   529444 Oct 22 10:42 halloweencatOG.png
-rw-r--r--   1 l  s      317 Oct 22 12:42 injectintopng.py
-rw-r--r--   1 l  s     1045 Oct 22 12:35 injectionWriteup.txt
-rw-r--r--@  1 l  s  2381232 Oct 22 11:19 procexp64.exe
```
Go ahead and open the modified halloweencat.png. Compare it to the OG. They look the same when you view it but, we can see from the size difference there is something up. 
Now lets extract exe from the png

```
❯ python3 extract.py
❯ ll
total 16080
drwxr-xr-x  12 l  s      384 Oct 22 13:16 .
drwxr-xr-x   3 l  s      96 Oct 22 12:47 ..
drwxr-xr-x  13 l  s      416 Oct 22 12:48 .git
-rw-r--r--   1 l  s       31 Oct 22 12:47 README.md
-rw-r--r--   1 l  s     3012 Oct 22 12:35 aboutPNG.txt
-rw-r--r--   1 l  s  2381232 Oct 22 13:16 evil.exe
-rw-r--r--   1 l  s      423 Oct 22 12:10 extract.py
-rw-r--r--@  1 l  s  2910676 Oct 22 13:15 halloweencat.png
-rw-r--r--@  1 l  s   529444 Oct 22 10:42 halloweencatOG.png
-rw-r--r--   1 l  s      317 Oct 22 12:42 injectintopng.py
-rw-r--r--   1 l  s     1045 Oct 22 12:35 injectionWriteup.txt
-rw-r--r--@  1 l  s  2381232 Oct 22 11:19 procexp64.exe
```
```
❯ shasum -a 256 evil.exe
8158dc0569972c10056f507cf9e72f4946600ce163c4c659a610480585cd4935  evil.exe
```
