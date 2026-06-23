class Animal():
    def __init__(self, name, sound):
        self.name = name
        self.sound= sound
    
    def speak(self):
        print(self.sound)
        
class Dog(Animal):
    def __init__(self, name, sound, owner):
        super().__init__(name, sound)
        self.owner = owner
        
    def speak(self):
        print('Con chó kêu')
        super().speak()
        
dog1 = Dog("Tuy", "Gâu Gâu", "A")
dog2 = Dog("Da", "Meo Meo", "B")
dog1.speak()
dog2.speak()