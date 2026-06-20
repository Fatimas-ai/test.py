with open("notes.txt","w") as f:
 f.write("hello fatima")

with open("notes.txt","r") as f:
 print(f.read()) 

 with open("notes.txt","a") as f:
  f.write("\nAI Engineer")  

with open("notes.txt","r") as f:
    print(f.read())

with open("notes.txt","r") as f:
    print(f.readline())
    print(f.readline())

with open("notes.txt","r")as f:
    print(f.readlines())





city=input("Enter city:")
with open("city.txt","w") as f:
    f.write(city)


with open("studnts.txt","r") as f:
    print(f.read.upper())