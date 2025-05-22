###########################################
# Ejercicio 1
###########################################

# Desarrollar clase Rectangulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def __eq__(self, other):
        return self.area() == other.area()

    def __lt__(self, other):
        return self.area() < other.area()
    
    def __gt__(self, other):
        return self.area() > other.area()
    

# Definir rectangulos para probar los metodos
A=Rectangulo(2,3)
B=Rectangulo(1,1)
C=Rectangulo(8,4)
D=Rectangulo(2,3)

# Comparaciones entre A y B
print(f"A == B: {A == B}")
print(f"A < B: {A < B}")
print(f"A > B: {A > B}")

# Comparaciones entre A y C
print(f"A == C: {A == C}")
print(f"A < C: {A < C}")
print(f"A > C: {A > C}")

# Comparaciones entre A y D
print(f"A == D: {A == D}")
print(f"A < D: {A < D}")
print(f"A > D: {A > D}")

# Comparaciones entre B y C
print(f"B == C: {B == C}")
print(f"B < C: {B < C}")
print(f"B > C: {B > C}")

# Comparaciones entre B y D
print(f"B == D: {B == D}")
print(f"B < D: {B < D}")
print(f"B > D: {B > D}")

# Comparaciones entre C y D
print(f"C == D: {C == D}")
print(f"C < D: {C < D}")
print(f"C > D: {C > D}")