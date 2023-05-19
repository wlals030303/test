# class Point:
#     def __init__(self,x=0,y=0):
#         self.__x = x
#         self.__y = y
    
#     def show(self):
#         print(f"{self.__x}, {self.__y}")
    
#     def set(self,x,y):
#         self.__x = x
#         self.__y = y

#     def get(self):
#         return (self.__x, self.__y)
    
# def test():
#     p1 = Point()
#     p2 = Point(2,3)

#     p1.show(); print()
#     p1.set(10,20); p1.show(); print()

#     p2.show(); print()

#     x,y = p2.get()
#     print(f"x={x}, y={y}")

# if __name__ == "__main__":
#     test()

class Time:
    def __init__(self,hour=0,minute=0):
        self.__hour = hour
        self.__minute = minute
    
    def display(self):
        print(f"{self.__hour:02d}:{self.__minute:02d}")

    def add(self,time):
        h = self.__hour + time.__hour
        m = self.__minute + time.__minute
        if m>=60:
            h += 1
            m -= 60
        return Time(h,m)

    @staticmethod
    def is_valid(hour,minute):
        if 0 <= hour < 24 and 0 <= minute < 60:
            return True
        return False

def main():
    t1 = Time(9)
    t2 = Time(9,30)

    t1.display()
    t2.display()

    later = t1.add(Time(1,15))
    later.display()

    if Time.is_valid(25,0):
        print("유호한 시각")
    else:
        print("유효하지 않은 시각")

if __name__ == "__main__":
    main()