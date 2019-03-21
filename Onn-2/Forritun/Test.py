class Reikna():
    def samlagning(tala1, tala2):
        return(tala1+tala2)

    def margfoldun(tala1, tala2):
        return(tala1*tala2)

    def deiling(tala1, tala2):
        return(tala1/tala2)

class Persona():
    def __init__(self, n, a, h):
        self.nafn = n
        self.aldur = a
        self.heimili = h

    def __str__(self):
        return("Nafn: " + self.nafn + "\nAldur:" + str(self.aldur) + "\nHeimili:" + self.heimili)

    def skrifaUt(self):
        print("Nafn:", self.nafn)
        print("Aldur:", self.aldur)
        print("Heimilir:", self.heimili)

p1 = Persona("Heimir", 14, "Tunguheiði")
p2 = Persona("Einar", 69, "Martröð")
print(p1)