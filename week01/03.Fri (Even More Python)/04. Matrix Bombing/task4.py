#Matrix Bombing
def build_matrix(rows, cols):
	matrix = []
	n = 1

	for i in range(rows):
		row = []

		for j in range(cols):
			row.append(n)
			n += 1
		else:
			matrix.append(row)

	return matrix

def matrix_bombing_plan(m):
	di = {}
	buf = 0
	N = len(m)
	M = len(m[0]) #or any other index
	
	for p in range(N):
		for q in range(M):
			summ = 0;
			for i in range(N):
				for j in range(M):
					if (
					((i == p-1) or (i == p) or (i == p+1)) and
					((j == q-1) or (j == q) or (j == q+1)) and 
					not (i == p and j == q)
					):
						buf = m[i][j] - m[p][q]
						if buf < 0:
							buf = 0
					else:
						buf = m[i][j]

					summ += buf
			di.update({"("+str(p)+ "," + str(q) + ")" : summ})

	print(di)

N = 3
M = 3
matrix = build_matrix(N,M)
matrix_bombing_plan(matrix)



