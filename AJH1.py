class Calcul:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2



class Plus(Calcul):
    def sum(self):
        result=self.num1+self.num2
        print("결과값: %d입니다."%(result))

class Minus(Calcul):
    def margin(self):
        result=self.num1-self.num2
        print("결과값: %d입니다."%(result))


class Mul(Calcul):
    def multiply(self):
        result=self.num1*self.num2
        print("결과값: %d입니다."%(result)) 

class Div(Calcul):
    def divide(self):
        if self.num2!=0:
            result=self.num1/self.num2
            print("결과값: %d입니다."%(result))
        else self.num2==0:
            print("you can't divide any number by zero")

class Normal_Stress(Div):
     def __init__(self,force,area):
             force=self.force
             area=self.area
             Nomral_stress=divide(force,area)
             

class Strain(Normal_Stress):
    def __init__(self,after_length,before_length):
        after_length=self.after_length
        before_length=self.before_length
        change=self.after_length-self.before_length
        strain=divide(self.change,self.before_length)

    
             

