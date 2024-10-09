class hinhchunhat:
    chuvi=None 
    dientich= None
    def __init__(self,chieudai , chieurong ):
        self.chieudai=chieudai
        self.chieurong=chieurong
        self.chuvi=None 
        self.dientich= None 

    @classmethod
    def nhapthongtin (self):
        self.chieudai=int (input('nhập chièue dài : '))
        self.chieurong=int (input('nhập chiều rộng : '))
    @classmethod
    def tinhchuvi (self):
        self.chuvi= self.chieudai*2 + self.chieurong*2 
        print ('tính chu vi ')
    @classmethod
    def tinhdientich (self):
        self.dientich= self.chieudai * self.chieurong
        print ('tính diện tích')
    @classmethod    
    def inthongtin (self):
        print ('chiều dài là :',self.chieudai)
        print ('chiều rộng là : ',self.chieurong)
        print ('chu vi là : ', self.chuvi)
        print ('diện tichs là : ',self.dientich)


while True : 
    print ('1:nhập thông tin ')
    print ('2:tính chu vi ')
    print ('3:tính diện tíchtích ')
    print ('4:in thông tin ')
    print ('5:thoát ')
    choice = int( input ('nhập lựa chọn: '))

    if choice == 1 :
        hinhchunhat.nhapthongtin()
    if choice==2 :
        hinhchunhat.tinhchuvi()
    if choice==3 :
        hinhchunhat.tinhdientich()
    if choice==4 :
        hinhchunhat.inthongtin()
    if choice==5 :
        break 