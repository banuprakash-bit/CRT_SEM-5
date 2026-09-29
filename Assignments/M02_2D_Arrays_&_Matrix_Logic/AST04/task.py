def diagonalSort(mat):
    rows = len(mat)
    cols = len(mat[0])

    # Process diagonals starting from the first column
    for start_row in range(rows):
        diagonal = []
        r, c = start_row, 0

        while r < rows and c < cols:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r, c = start_row, 0
        i = 0
        while r < rows and c < cols:
            mat[r][c] = diagonal[i]
            i += 1
            r += 1
            c += 1

    # Process diagonals starting from the first row
    for start_col in range(1, cols):
        diagonal = []
        r, c = 0, start_col

        while r < rows and c < cols:
            diagonal.append(mat[r][c])
            r += 1
            c += 1

        diagonal.sort()

        r, c = 0, start_col
        i = 0
        while r < rows and c < cols:
            mat[r][c] = diagonal[i]
            i += 1
            r += 1
            c += 1

    return mat


if __name__ == '__main__':
    m, n = map(int, input().split())

    mat = []
    for i in range(m):
        mat.append(list(map(int, input().split())))

    result = diagonalSort(mat)

    for row in result:
        print(*row)