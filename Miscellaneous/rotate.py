#short code for rotating 90 degrees clockwise
def rotate90Clockwise(m):
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]
def rotate90Anticlockwise(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]
