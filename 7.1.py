import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        x = ''  # Создаём пустую строку, в которую будем записывать нашу матрицу в необходимом формате
        for i in range(len(self.matrix)):
            x = x + '\t'.join(map(str, self.matrix[i])) + '\n'
        return x

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):  # Если у матриц разный размер возвращаем None
            return None
        res = copy.deepcopy(self.matrix)  # Создадим копию матрицы, в неё будем записывать результат сложения
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


l1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Матрица 1
l2 = [[11, 22, 33], [44, 55, 66], [77, 88, 99]]  # Матрица 2
m = Matrix(l1)  # Создаём объект m с матрицей l1
s = Matrix(l2)  # Создаём объект s с матрицей l2
print(m)
print(s)
z = m + s
print('Результат сложения матриц')
print(z)
