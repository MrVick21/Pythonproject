class divb:
    school="symbiosis" #class attribute
    def __init__(obj,name):
        obj.name=name
    def hello(self):
        print("Hello")
   
s1=divb("Shreya") #$object create
print(s1.name,s1.school)
s2=divb("ojas")
print(s2.name,s2.school)
s3=divb("aryan")
print(s3.name,s3.school)

