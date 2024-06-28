class Divison_B:

    def __init__(object,name,address,blood_grup):#parameterix
        object.name=name
        object.city=address
        object.blood=blood_grup
        print(object.name,object.blood,end=" ")
        print(object.city)
    @staticmethod
    def __hello__(self,name,address,blood_grup):
        print("Hello")
s1=Divison_B("shreya","pune","A+")#students
s2=Divison_B("ojas","Mumbai","O+")
s1.hello("","","")

