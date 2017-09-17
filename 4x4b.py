#!/usr/bin/python
import numpy as np
def search(matrix,x,y):
	zerosx=[]
	zerosy=[]
	for i in range(1,5):
		if matrix[x][i]==0:
			zerosx.append(i)
		if matrix[i][y]==0:
			zeroy.append(i)
	return zerosx,zerosy

clues = (2,2,1,3,2,2,3,1,1,2,2,3,3,2,1,3)
matrix = [[0 for x in range(6)] for y in range (6)]
for i in range(4):
	matrix[0][i+1]=clues[i]
	matrix[i+1][5]=clues[i+4]
	matrix[5][i+1]=clues[-i-5]
	matrix[i+1][0]=clues[-i-1]

for i in range(1,5):
	if (matrix[0][i]+matrix[5][i])==5:
			matrix[matrix[0][i]][i]=4
	if (matrix[i][0]+matrix[i][5])==5:
			matrix[i][matrix[i][0]]=4
#zx,zy=search(matrix,)



#if clues[i] == 4:
#		if i<=3:
#			matrix[0][i], matrix[1][i], matrix[2][i], matrix[3][i] = 1, 2, 3, 4
#		elif i<=7:
#			matrix[i-4][3], matrix[i-4][2], matrix[i-4][1], matrix[i-4][0] = 1, 2, 3, 4
#		elif i<=11:
#			matrix[3][11-i], matrix[2][11-i], matrix[1][11-i], matrix[0][11-i] = 1, 2, 3, 4
#		else:
#			matrix[15-i][0], matrix[15-i][1], matrix[15-i][2], matrix[15-i][3] = 1, 2, 3, 4
#	if clues[i]==1 :
#		if i <= 3:
#			matrix[0][i] = 4
#		elif i<=7:
#			matrix[i-4][3] = 4
#		elif i<=11:
#			matrix[3][11-i] = 4
#		else:
#			matrix[15-i][0] = 4'''

for x in range(6):
	print("{0}  {1}  {2}  {3}  {4} {5}"\
	.format(matrix[x][0], matrix[x][1], matrix[x][2],\
	        matrix[x][3],matrix[x][4],matrix[x][5]))
