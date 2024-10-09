class stack : 
    nganxep = []
    phantu = None 

    def __init__(self):
        self.nganxep=[]

    def __del__(self):
        print ("đối tượng đã bị xóa ")

    def push ( self):
        while True :
            print ('1:nhập phần tử ')
            print ('2:dừng lại ')
            
            choice = int(input ('Nhập lựa chọn :  '))
            if choice ==1  : 
                self.nganxep.append(input('Nhập thêm phần tử : '))
            if choice == 2 :
                break 
    def pop (self ): 
        print ( 'phần tử của ngăn xếp là : ', self.nganxep[-1])
    
    def capphatmang (self ):
        self.phantu=int (input ("nhấp ố phần tử của mãng : "))

    def ktra ( self ): 
         if len(self.nganxep)> self.phantu:
              print(self.nganxep)
              print ( ' mãng đã đầy ')
    
    def count (self ): 
        print ( 'số phần tử trong mãng là :  ',len ( self.nganxep))

    def innoidung  (self):
        print ('nội dung của ngăn xếp:  ',self.nganxep)
              


obj = stack()
obj.capphatmang()
obj.push()
obj.pop()
obj.ktra()
obj.count()
obj.innoidung()