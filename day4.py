class person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name:",self.name)
class student(person):
    pass
s1=student("Fatima")       
s1.show_name()    

class Animal:
    def __init__(self,name):
        self.name=name
class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name) 
        self.breed=breed
d1=Dog("tom","german")
print(d1.name)   
print(d1.breed)      

class animal:
    def speak(self):
        print("animal soung")
class dog(animal):
    def speak(self):
        print("bark") 
d1=dog()
d1.speak()              

class student:
    def __init__(self):
        self._name="Fatima"
s1=student()
print(s1._name)    

class person:
    def __init__(self,name):
        self.name=name
    def show_name(self):
        print("Name:",self.name)    
class teacher(person):
    def __init__(self,name,salary):
        super().__init__(name) 
        self.__salary =salary 
    def get_salary(self):
        return self.__salary
t1=teacher("fatima",10000) 
t1.show_name()  
print("salary:",t1.get_salary())
             