import re

def create_matrix():
    matrix = []

    with open('day4.txt', 'r') as file: 
        for line in file:
            matrix.append(line.strip())
    
    return matrix

def check_horizontal(matrix, pattern):
    occurences = 0
    for line in matrix:
        occurences += len(re.findall(pattern, line))
        occurences += len(re.findall(pattern, line[::-1]))
    
    return occurences

def check_vertical(matrix, pattern):
    occurences = 0
    for i in range(len(matrix[0])):
        col = ''.join(row[i] for row in matrix)
        occurences += len(re.findall(pattern, col))
        occurences += len(re.findall(pattern, col[::-1]))

    return occurences
    
def check_diagonal(matrix, pattern):
    rows, cols = len(matrix), len(matrix[0])
    occurences = 0

    for d in range(rows - 3):
        for i in range(cols - 3):
            diagonal = ''.join([
                matrix[d][i],
                matrix[d + 1][i + 1],
                matrix[d + 2][i + 2],
                matrix[d + 3][i + 3]
            ])
            if diagonal == pattern or diagonal == pattern[::-1]:
                occurences += 1

    for d in range(rows - 3):
        for i in range(3, cols):
            diagonal = ''.join([
                matrix[d][i],
                matrix[d + 1][i - 1],
                matrix[d + 2][i - 2],
                matrix[d + 3][i - 3]
            ])
            if diagonal == pattern or diagonal == pattern[::-1]:
                occurences += 1

    return occurences

if __name__ == "__main__":
    pattern = r"XMAS"
    matrix = create_matrix()
    matches = check_horizontal(matrix, pattern)
    matches += check_vertical(matrix, pattern)
    matches += check_diagonal(matrix, pattern)
    print(matches)
