# Xaay dựng lớp
class Stack:

    # hàm khơi tạo
    def __init__(self):
        self.s = []

    # hàm bổ sung
    def push(self, x):
        self.s.append(x)

    # Hamf loại bỏ
    def pop(self):
        if len(self.s) == 0:
            return "stack is empty"                     
        return self.s.pop()

    # hàm kiểm tra ngăn xêps dỗng
    def is_empty(self):
        return len(self.s) == 0


    # hàm kiểm tra ngăn
S = Stack()
S.push(int(input('nhập phần tử : ')))
S.pop()
S.is_empty()