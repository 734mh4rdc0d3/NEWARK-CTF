import os

for i in range(1000 , 0 , -1):
	file = open("direction.txt")
	dir = file.read()
	print(dir)
	file.close()
	filename = str(i)+dir+".zip"
	os.system("unzip -o "+filename)
