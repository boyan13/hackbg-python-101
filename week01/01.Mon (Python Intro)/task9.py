#Sum Numbers in Matrix
def sum_matrix(m):
	msum = 0

	for i in range(len(m)):
		for j in range(len(m[0])):
			msum += m[i][j]

	return msum

m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
m3 = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

print( sum_matrix(m1) )
print( sum_matrix(m2) )
print( sum_matrix(m3) )