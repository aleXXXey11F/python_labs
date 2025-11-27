m = [[1, 2], [3]]


def transpose(mat: list[list[float | int]]) -> list[list]:
    if not m:
        return m
    for i in range(len(m)):
        if len(m[i]) != len(m[0]):
            raise ValueError("Матрица рваная")
    transposed = list(map(list, zip(*m)))
    return transposed


def row_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(m)):
        if len(m[i]) != len(m[0]):
            raise ValueError("Матрица рваная")
    rowsums = [sum(row) for row in m]
    return rowsums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in range(len(m)):
        if len(m[i]) != len(m[0]):
            raise ValueError("Матрица рваная")
    colsums = []
    for j in range(len(m[0])):
        col_sum = 0
        for i in range(len(m)):
            col_sum += m[i][j]
        colsums.append(col_sum)
    return colsums


try:
    print(transpose(m))
except ValueError as e:
    print(f"Ошибка: {e}")  # transpose output

try:
    print(row_sums(m))
except ValueError as a:
    print(f"Ошибка: {a}")  # row_sums output

try:
    print(col_sums(m))
except ValueError as b:
    print(f"Ошибка: {b}")  # col_sums output
