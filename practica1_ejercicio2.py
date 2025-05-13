#Generando matriz tridimensional H
import numpy as np
H = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(H)

H.transpose(0,2, 1)