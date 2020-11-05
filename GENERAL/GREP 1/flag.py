file = open("flag.txt")

for line in file:
	if(len(line[:-1]) == 52 and set(line[:-1][6:16])==set(['n','a','c']) and set(line[:-2][-14:])==set(['c','t','f']) ):
		print(line[:-1])