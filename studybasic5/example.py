class FourCal:   #부모 클래스
    first = 2  #클래스 변수
    second = 3
   # def __init__(self, first, second):
    #    self.first = first  #객체 변수
     #   self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
a = FourCal()
print(a.first)
b = FourCal()
print(b.first)