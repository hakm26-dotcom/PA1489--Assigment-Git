"""
Det här är project för Mjukvarutveckling Grundläggande


"""
class Nummer:
    def __init__ (self, x):
        self.myNumber = x

    def smallerThan(self, x):
        return self.myNumber < x
    
    def get(self):
        return self.myNumber 
    
    def __str__(self):
        return f"Nummer {self.get()}"