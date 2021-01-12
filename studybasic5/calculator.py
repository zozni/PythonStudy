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
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

class SafeFourCal(FourCal): #자식 클래스 div가 부모한테 있는데 이걸 한번더 정의함.
    def div(self):           #자식이 우선시 된다. 그냥 나누는게 아니라 0으로 나누면 안되니까가 추가됨.
        if self.second == 0:
            return 0
        else:
            return self.first/self.second

class MoreFourCal(FourCal): #자식 클래스
    def pow(self):  #부모에게 없는 기능
        result = self.first ** self.second #지수
        return result
a = MoreFourCal(4, 2)
print(a.pow())