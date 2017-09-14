#!/usr/bin/python

clues = (2,2,1,3,2,2,3,1,1,2,2,3,3,2,1,3)
matrix = [[0 for x in range(4)] for y in range (4)]
for i in range(0,16):
	if clues[i]==1:
		print "ok"
		if i<=3:
			matrix[0][i] =4
		elif i<=7:
			matrix[i-4][3]=4
		elif i<=11:
			matrix[3][11-i]=4
		else:
			matrix[15-i][0]=4
	elif clues[i]==4:
		if i<=3:
			matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i] =1,2,3,4
		elif i<=7:
			matrix[i-4][3],matrix[i-4][2],matrix[i-4][1],matrix[i-4][0]=1,2,3,4
		elif i<=11:
			matrix[3][11-i],atrix[2][11-i],atrix[1][11-i],atrix[0][11-i]=1,2,3,4
		else:
			matrix[15-i][0],matrix[15-i][1],matrix[15-i][2],matrix[15-i][3]=1,2,3,4
for x in range(4):
	print "{0:d}  {1:d}  {2:d}  {3:d}".format(matrix[x][0],matrix[x][1],matrix[x][2],matrix[x][3])
