class Calcul:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

class Calcul1(Calcul):
    def sum(self):
        result=self.num2+self.num1
        return result

a=Calcul1(10,20)
a.sum()
print(a.sum())
