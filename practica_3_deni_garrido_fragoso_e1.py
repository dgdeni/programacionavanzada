import math
#Creando la clase Vector
class Vector:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  
#Método que calcula la magnitud del Vector usando la fórmula r = (x^2 + y^2)^1/2
#def magnitud(self):
 # return(self.x**2 + self.y**2)**0.5

  def magnitud(self):
    return math.sqrt(self.x**2 +self.y**2)
 
#Método que calcula el ángulo en radianes utilizando la fórmula θ = arctan(y/x)

  def ang_rad(self):
    return math.atan2(self.y,self.x)

#Método que calcula el ángulo en grados

  def ang_grados(self):
    return math.degrees(self.ang_rad())

#Sumando Vectores utilizando la función add
  
  def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

#Vector en forma (x,y)

  def __str__(self):
    return f'({self.x,self.y})'


#Validando programa con ejemplo
#Primero vector p
p = Vector(5, -1)

print(f"p={p}")
print(p.magnitud())
print(p.ang_rad())
print(p.ang_grados())

#Ahora vector q
q = Vector(2,-4)

print(f"q={q}")
print(q.magnitud())
print(q.ang_rad())
print(q.ang_grados())

#Suma de ambos vectores
print(p+q)