class ts : 
    thongtin=[]
    tongdiem=None 
    def __init__(self,hoten , diemtoan , diemly , diemhoa ) :
        self.hoten =hoten
        self.diemtoan=diemtoan 
        self.diemly = diemly 
        self.diemhoa = diemhoa  

    @classmethod
    def nhapthongtin (self): 
        self.hoten =input ('nhập tên :')
        self.diemtoan=int (input ('nhập điểm toán : ')) 
        self.diemly = int (input ('nhập diểm toán : '))
        self.diemhoa = int (input ('nhập điểm hóa : '))
        self.thongtin.append({'ten ': self.hoten,
                              'diemtoan':self.diemtoan,
                              'diemly':self.diemly,
                              'diemhoa':self.diemhoa,
                              'tongdiem':ts.tinhtongdiem()})

    @classmethod 
    def inthongtin (self): 
        print ('tên thí sinh : ',self.hoten)
        print ('điểm lý : ',self.diemly)
        print ('điểm toán : ',self.diemtoan)
        print ('điểm hóa : ',self.diemhoa)
    
    @classmethod
    def tinhtongdiem (self ):
        self.tongdiem = self.diemhoa + self.diemly + self.diemtoan
        print ('tổng điểm là : ',self.tongdiem)
        return self.tongdiem
      

diemchuan = 20 

while True : 
    print ('1:nhập thông tin thí sinh : ')
    print ('2:thoát ')
    choice = int (input ("nhập lựa chọn : "))
    if choice== 1 : 
        ts.nhapthongtin()
        ts.inthongtin()
        ts.tinhtongdiem()
        
       
    if choice == 2 : 
       break 

danhsachtrungtuyen=ts.thongtin.copy()
for i in danhsachtrungtuyen:
    if i['tongdiem']<diemchuan:
        danhsachtrungtuyen.remove(i) 
danhsachchinhsua = sorted(danhsachtrungtuyen, key=lambda x: x['tongdiem'], reverse=True)

print (danhsachchinhsua)