###########################################
# Ejercicio 2
###########################################

class Playlist:
    def __init__(self, canciones):
        self.canciones = canciones
    
    def __len__(self):
        return len(self.canciones)
    
    def __getitem__(self, index):
        return self.canciones[index]

    def __setitem__(self, index, value):
        self.canciones[index] = value

# Definir Playlist para probar metodo
canciones = ["Cancion 1", "Cancion 2", "Cancion 3", "Cancion 4", "Cancion 5"]
playlist = Playlist(canciones)
print("Cancion en el indice 3: ", playlist.__getitem__(3))
print("Cancion en el indice 3: ", playlist[3])
playlist.__setitem__(3, "Cancion 6")
print("Canciones en la playlist: ",playlist.canciones)
playlist[0]="Cancion final"
print("Canciones en la playlist: ",playlist.canciones)
