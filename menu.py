#como seguir:hacer que los botones reciban bien los datos y funque el get rect,entender si se necesita un rect del texto,deberia poder pasardatos sin ponerlo en variable
#el cuadrado de texto y el texto necesitan rect para poder ubicarlo
#las x e y cambian segun si pones center u otra cosa,hay q ir probando
import pygame
import sys
from boton import Boton
MOUSE_POS= []*2
fondo= pygame.image.load("imagenes/fondo inicio.jpg") 
fondo= pygame.transform.scale(fondo, (1280, 720))#declaro la variable fondo como imagen
pantalla=pygame.display.set_mode((1280, 720))  
imagenboton=pygame.image.load("imagenes/boton.jpg")#esta medio al pedo porque no consigo pasarlo por parametro
global volver
volver= Boton(imagenboton ,1100,600)

pos=(640,250)
def menu():
    seguir=True
    pygame.display.init()
    pygame.display.set_caption("Menu de prueba")
    Bplay= Boton(imagenboton ,pos[0],pos[1])
    while seguir==True:
         reloj = pygame.time.Clock()
         pantalla.blit(fondo, (0, 0))# podes en vez de esto poner pantalla.fill("black")
         
         MENU_TEXT = titulos(100).render("menu principal", True, (20, 113, 103) )
         MENU_RECT= MENU_TEXT.get_rect(center=(640,100)) 
         
         PLAY= titulos(70).render("Jugar", True, (50, 50, 50) )
         rect_play = PLAY.get_rect(center=(640,250)) 

         pantalla.blit(MENU_TEXT, MENU_RECT)
         Bplay.dibujar(pantalla)
         
         pantalla.blit(PLAY, rect_play)#el orden este determina que se dibuja arrina de que
         pygame.display.update()       # Actualiza la ventana
         pygame.display.flip()
        
         for evento in pygame.event.get():
            if evento.type== pygame.MOUSEBUTTONDOWN:
                MOUSE_POS= pygame.mouse.get_pos()
                if Bplay.click(MOUSE_POS)==True:#que aca se llame a un pantallajugar() que sea otro def
                    jugar()
                    

            if evento.type == pygame.QUIT:
                seguir = False
         reloj.tick(400)
def jugar():
    seg=True
    while seg==True:
        pantalla.fill("black")
        #cartel=pygame.image.load("imagenes/efd7670061ca9e740268ddc530ce88f5.png")
        #cartelrect=cartel.get_rect(center=(640,250))
        HISTORIA= titulos(50).render("el dia de rayita empezo como cualquier otro...", True, (240, 113, 1))
        HIS_RECT= HISTORIA.get_rect(bottomleft=(0,700))  #linea de arriba y esta escriben el titulo, rect es de rectangulo
        pantalla.blit(HISTORIA,HIS_RECT)
        boton_volver(volver)
        pygame.display.update()
        for evento in pygame.event.get():
            if evento.type==pygame.MOUSEBUTTONDOWN:
                MOUSE_POS= pygame.mouse.get_pos()
                if volver.click(MOUSE_POS)==True:
                    seg = False
                else:seg= historia1(seg)

def historia1(seg):
    seg1=True 
    while seg1==True: 
        pantalla.fill("black") 
        historia1= titulos(50).render("te caiste al mar por boluda y te ahogaste", True, (240, 113, 1)) 
        HIS1_RECT= historia1.get_rect(bottomleft=(0,700)) 
        pantalla.blit(historia1,HIS1_RECT) 
        boton_volver(volver)
        pygame.display.update() 
        for evento in pygame.event.get(): 
            if evento.type==pygame.MOUSEBUTTONDOWN: 
                MOUSE_POS= pygame.mouse.get_pos()
                if volver.click(MOUSE_POS)==True:
                    seg1=False
                    return False
                    
                    

def boton_volver(volver):
    volver.dibujar(pantalla)
    VOLVE= titulos(70).render("Volver", True, (45, 45, 45) )
    rect_VOLVE= VOLVE.get_rect(center=(1100,600)) 
    pantalla.blit(VOLVE,rect_VOLVE)
def titulos(tamanio):
    pygame.font.init()#debuelve la frase en la fuente y tamanio adecuado, hay que pasar el tam
    return pygame.font.SysFont("timesnewroman", tamanio)

         
         
    pygame.quit()
    sys.exit()

menu()

