import math 
class diem :
    def gioithieu(self):
        print ('đây là lớp điểm ')


class elip (diem):
    def __init__(self,truclon , trucnho ) -> None:
        super().__init__()
        self.truclon=truclon 
        self.trucnho = trucnho

    def tinhdientich (self):
        self.dientich= ((self.trucnho+self.truclon)/2)* math.pi 

class tron(elip):
  def __init__(self, truclon , trucnho=None,) -> None:
      super().__init__(truclon, trucnho )
  
  def tinhdientich(self):
      self.dientich=  (math.pi**2 ) *(self.truclon/2)

obj1=diem()
obj2=elip(7,5)
obj2.tinhdientich()
print (obj2.dientich)
obj3=tron(4)
obj3.tinhdientich()
print (obj3.dientich)