def add(a, b):
    return a + b

print(add(10, 20))

def add(a, b):
    print(a+b)
add(5, 3)

def check(num):
    if num % 2 == 0:
     return "Even"
    else:
     return "odd"
print(check(7))         

def check(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check(7))

student = {
    "name": "Fatima",
    "age": 18,
    "marks": {
        "Math": 90,
        "English": 85,
        "Science": 95
    }
}

print(student["name"])
print(student["marks"]["Math"])

def check_num(num):
    if num>0:
        return "positive"
    elif num<0:
        return "negative"    
    else:
        return "zero"
print(check_num(-5))        

def average(a,b,c):
    return(a+b+c)/3
print(average(5,4,3))    


def average(a, b, c):
    return (a + b + c) / 3

print(average(10, 20, 30))

def square_cube(num):
    return num**2, num**3

print(square_cube(3))

student={
    "Name":"Fatima",
    "Marks":{
        "Math":50,
        "science":60,
    }
}
print(student["Marks"]["science"])


def average(numbers):
    return sum (numbers)/len (numbers)
print(average([1,2,3]))    
