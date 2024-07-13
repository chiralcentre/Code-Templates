#short code for rotating 90 degrees clockwise
def rotate90Clockwise(m):
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]

def rotate90Clockwise(matrix):
    r = len(matrix)
    for i in range(r // 2):
        for j in range(i, r - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[r - 1 - j][i]
            matrix[r - 1 - j][i] = matrix[r - 1 - i][r - 1 - j]
            matrix[r - 1 - i][r - 1 - j] = matrix[j][r - 1 - i]
            matrix[j][r - 1 - i] = temp
    return matrix

def rotate90Anticlockwise(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
