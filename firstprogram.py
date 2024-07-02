class card:
    def __init__(self,accnum,password):
        self.accnum=accnum
        self.__password=password #private atrribute
        print(self.accnum,self.__password)
        self.__hello()
    def __hello(self): #private method
        print("Private Method")


customer=card(34567,"vik123")
print("Masta jhala Kaam")
