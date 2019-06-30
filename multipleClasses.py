class Animal:
    def Animalspeak(self):
        print ("Animal is speaking")
class Humanbeing:
    def Humanspeak(self):
        print ("Human is speaking")
class Living(Animal,Humanbeing):
    def live(self):
        print ("all live is speaking")
obj = Living()
obj.live()
obj.Humanspeak()
obj.Animalspeak()