class Alumno:
    nombre = ""
    nota = ""
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def aprobado(self):
        if self.nota >= 5:
            print("Aprobado")

a = Alumno("Paco", 6)
print(a.nombre, a.nota)
a.aprobado()