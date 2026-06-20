class Book:
     def __init__(self, title, author):
        self.title = title
        self.author = author
     def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
b1 = Book("Python Basics", "Fatima")
b1.display()

class Mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def show(self):
        print("Brand:",self.brand) 
        print("Price:",self.price)  
m1=Mobile("apple",12000)    
m1.show()    

class Dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):
        print(self.name, "is barking")  
d1=Dog("Tom","German shepherd") 
d1.bark()        

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):    
        return 3.14 * self.radius * self.radius
c1 = Circle(5)
print("Area =", c1.area())   

class product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def discount(self,percent):
        discount_amount=self.price*percent/100
        new_price=self.price-discount_amount
        print("New price:",new_price) 
p1=product("Laptop",10000)  
p1.discount(10)

class Library:
    def __init__(self,book_name,author,pages):
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def display(self):
        print("Book_Name:",self.book_name) 
        print("Author:",self.author)  
        print("pages:",self.pages)
    def is_big_book(self):
        if self.pages > 300:
            print("Big Book")  
        else:
            print("not big book")
book1=Library("Python","Fatima",350)
book1.display()
book1.is_big_book()

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Name:",self.name)  
        print("Marks:",self.marks)  
    def calculate_grade(self):   
        if self.marks>90:
            print("A+")
        elif self.marks>80:
            print("A")   
        elif self.marks>70:
            print("B")
        elif self.marks>60:
            print(C)    
        else:
            print("faii")   
s1=student("Fatima",75)
s1.display()
s1.calculate_grade()    
            
