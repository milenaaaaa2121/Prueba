import pygame
class ima:
    def __init__ (self,im):
        self.imagen=im
    def imprime(self):
        print(type(self.imagen))
pygame.init()
try:
    # Cargar la imagen
    imagen = pygame.image.load("imagenes\\2023-12-31.png")
except pygame.error as e:
    print(f"Error al cargar la imagen: {e}")
    imagen = None

if imagen:  # Verificar si la imagen se cargó correctamente
    prueba = ima(imagen)
    prueba.imprime()
else:
    print("No se pudo cargar la imagen.")