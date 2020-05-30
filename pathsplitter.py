#/usr/bin/python3

pth = open( "path.txt" ).read()
folders = pth.split(';')
for f in folders:
    print(f)
    