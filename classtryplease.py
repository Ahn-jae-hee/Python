#연비를 property로?!
#class car 내에 function을 만들던가?!
#도요타,현대 이런거?!

class Car:
    def __init__(self):
        self.__color="None"
        self.__company="None"
        self.__car_model="None"
        self.__speed=0
        self.__fuel=0   

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def company(self):
        return self.__company

    @company.setter 
    def company(self,company):
        self.__company=company

    @property
    def fuel_efficiency(self):
        

    @property
    def car_model(self):
        return self.__car_model

    @car_model.setter

    def car_model(self,car_model):
        self.__car_model=car_model


   # @property

   # def speed(self):
     #   return self.__speed

   # @speed.setter        
    
   # def speed(self,speed):
    #    self.__speed=speed

    @method  
    def honk(self):
        return "빠라바라빠라밤"

    def up_Speed(self, up_value):
        self.__speed += up_value
        if self.speed>=200:
            self.speed=200
        return self.speed

    def down_Speed(self,down_value):
        self.__speed -=down_value
        if self.speed<0:
            self.speed=0
        return self.__speed  

    def charge_fuel(self,fuel):
        self.__fuel+=fuel
        return self.__fuel

    def drive(self, distance):
        self.__fuel-=distance*0.02
        if self.__fuel<0:
            self.__fuel=0   c
            return "not enough energy"
        else: 
            return self.__fuel

                
class Bicycle:
    
    def __init__(self): 

        self.__color="None"
        self.__numberofwheels=0        
        self.__company="None"

    #def set_info(self,color,numberofwheels,company):
        #self.__color=color
        #self.__numberofwheels=numberofwheels
        #self.__company=company

    #def get_info(self):
        #return self.__color, self.__numberofwheels, self.__company
       
    @property
    
    def color(self):
        return self.__color
    
    @color.setter
    def color(self,color):
        self.__color=color

    @property
    def numberofwheels(self):
        return self.__numberofwheels

    @numberofwheels.setter    
    def numberofwheels(self,numberofwheels):
        self.__numberofwheels=numberofwheels


    @property

    def company(self):
        return self.__company

    @company.setter

    def company(self,company):
        self.__company=company


if __name__ == '__main__':  #name=main 좀 더 찾아보기!!
    #검색을 해보면서 알아보면서 생각을 하면서 알아내야 한다!!!
    #namespace: import 이 파일을 라이브러리화해서 이 파일에 있는 클래스를 빼오겠다
    #namespace 라는 것은 결국에는 name을 얘기하는 것. 
    #컴퓨터인식을 하기 위해서 구별하는 것 
    #namespace: 함수만 가져와도 된다. 
    #이름공간. 
   
    a=Car()
    b=Bicycle()
    a.color="Red"
    print(a.color,a.company)








