class divb:
    name="anonymous" #class attribute
    school="Symbiosis"
    def __init__(self,name,marks):
        self.name=name #  #object attribute> class attribute   
        self.marks=marks
        print("Adding in databases....")

s1=divb("shreya",97)
print(s1.name)


