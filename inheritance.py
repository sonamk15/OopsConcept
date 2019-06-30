# multilevel classes
class Firstgenration:
    def dada(self):
        print ("my dada")
class  Secondgenration(Firstgenration):
    def papa(self):
        print ("my papa")
class Thridgenration(Secondgenration):
    def myself(self):
        print ("i am")
obj = Thridgenration()
obj.myself()
obj.papa()
obj.dada()

