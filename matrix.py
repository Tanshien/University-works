# 需要创建一个矩阵类进行矩阵运算

class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix

    def add(self,n):
        # n为需要加上的常数

        result = [[self.matrix[i][j] + int(n)
                   for j in range(len(self.matrix[0]))] # j为列数
                   for i in range(len(self.matrix))] # i为行数
        # 创建列表生成式，即进行加法后的矩阵

        print(f"加法后的矩阵为\n{result}")
        # 打印矩阵

    def subtract(self,n):
        result = [[self.matrix[i][j] - int(n)
                   for j in range(len(self.matrix[0]))]  # j为列数
                   for i in range(len(self.matrix))]  # i为行数
        # 创建列表生成式，即进行减法后的矩阵

        print(f"减法后的矩阵为\n{result}")
        # 打印矩阵

    def multiply(self,n):
        result = [[self.matrix[i][j] * int(n)
                   for j in range(len(self.matrix[0]))]  # j为列数
                   for i in range(len(self.matrix))]  # i为行数
        # 创建列表生成式，即进行乘法后的矩阵

        print(f"乘法后的矩阵为\n{result}")
        # 打印矩阵

    def divide(self,n):
        if n != 0:
            result = [[self.matrix[i][j] / int(n)
                       for j in range(len(self.matrix[0]))]  # j为列数
                       for i in range(len(self.matrix))]  # i为行数
            # 创建列表生成式，即进行除法后的矩阵

            print(f"乘法后的矩阵为\n{result}")
            # 打印矩阵

        else:
            print("除数不能为0！")

Alist = Matrix([[1,2,3],[4,5,6]])

while True:
    print(f"当前矩阵为{Alist.matrix}")
    sign = input("请选择你想进行的运算(若需要停止此程序则输入0）：\n"
                 "A:加法\nB:减法\nC:乘法\nD:除法\n")
    if sign == '0':
        print("矩阵计算程序已结束！")
        break

    num = input("请输入你想进行运算的数字：\n")

    if sign == 'A':
        Alist.add(num)
    elif sign == 'B':
        Alist.subtract(num)
    elif sign == 'C':
        Alist.multiply(num)
    elif sign == 'D':
        Alist.divide(num)