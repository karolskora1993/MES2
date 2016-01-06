class Solver(object):
    @staticmethod
    def solve(A, b):
		n=len(A)
		L = [[0]*n for i in range(0, n)]
		D = [[0]*n for i in range(0, n)]
		U = [[0]*n for i in range(0, n)]
		x = [0 for i in range(0, n)]

		for i in range(0,n):
			for j in range(0,n):
				if i<j:
					U[i][j] = A[i][j]
                elif i > j:
					L[i][j] = A[i][j]
				else:
					D[i][j] = A[i][j]

		for i in range(0, n):
			D[i][i] = 1 / D[i][i]

		for i in range(0, n):
			b[i] *= D[i][i]

		for i in range(0,n):
			for j in range(0,n):
				L[i][j] *= D[i][i]

		for i in range(0,n):
			for j in range(0,n):
				U[i][j] *= D[i][i]


		for k in range(0,self.__accuracy):
			for i in range(0,n):
				x[i] = b[i]
				for j in range(0,n):
					x[i] -= L[i][j] * x[j]
				for j in range(i+1, n):
					x[i] -= U[i][j] * x[j]

	return x