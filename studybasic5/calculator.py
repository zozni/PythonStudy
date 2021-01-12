class FourCal:   #부모 클래스
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal): #자식 클래스
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4, 2)
print(a.add())