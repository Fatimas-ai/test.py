  # function
def square(num):
    return num*num
print(square(5))  

def check(num):
    if num%2==0:
        return "even"
    else:
        return"odd"
print(check(7))   
 # lambda
multiply=lambda a,b:a*b
print(multiply(5,4)) 
 # *args
def total(*args):
    return sum(args)
print(total(1,2,3,4,5))
 # arguments
def add(a,b,c,d,e):
    return a+b+c+d+e
print(add(1,2,3,4,5))   
 # **kwargs
def students(**info):
    print(info)
students(name="Fatima",age=20)    

 # Day2
 # list using comprehension
even=[x for x in range(2,21,2)] 
print(even)
# dicionary comprehension
cube={x:x**3 for x in range(1,6)}
print(cube)
# common element
A={1,2,3,4}
B={4,5,7,1}
print(A&B)
# Day3
class car:
    def __init__(self,brand,model):
     self.brand=brand
     self.model=model
    def show(self):
     print(self.brand,self.model)     
c1=car("Toyota",2021)
c1.show()

class student:
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def average(self):
        return(self.m1+self.m2+self.m3)/3
s1=student("Fatima",90,89,95) 
print(s1.average())
#Day4
class animal:
    def sound(self):
        print("animal sound")

class dog(animal):
    def sound(self):
        print("bark")        
dog().sound()     

class employee:
    def __init__(self,salary):
     self.__salary=salary
    def get_salary(self):
        return self.__salary
e1=employee(3000)  
print(e1.get_salary())       
# Day5
with open("data.txt","w")as file:
    file.write("hello ai")

try:
    print(10/0)    
except ZeroDivisionError:
    print("cannot divide")    