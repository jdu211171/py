N = 6

matrix = [[0]*N for _ in range(N)]

for i in range(N):
    matrix[i][i] = 1
    matrix[i][N-i-1] = 1

for row in matrix:
    print(' '.join(str(x) for x in row))


