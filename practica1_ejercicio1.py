import numpy as np

#Arreglo tridimensional de tamaño 5x4x3 con valores aleatorios entre 0 y 100
arreglo = np.random.randint(101, size= (5,4, 3))
print(arreglo)

#Elemento más pequeño y más grande
e_min = np.min(arreglo)
e_max = np.max(arreglo)
print(e_min)
print(e_max)

#Ubicación
ub_min = np.where(arreglo == e_min)
ub_max = np.where(arreglo == e_max)
print(ub_min)
print(ub_max)
