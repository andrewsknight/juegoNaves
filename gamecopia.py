
import pygame as pg

pg.init()

class Nave():
    def __init__(self, padre, x, y):
        self.imagen = pg.image.load("./img/cannon.png")
        self.rect = self.imagen.get_rect()
        self.padre = padre
        self.x = x
        self.y= y
    
        
        self.vx = 5
    
    def dibujar(self):
        
        self.padre.blit(self.imagen,(self.x, self.y))
        

    def mover(self):
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.x -= self.vx
        if teclas[pg.K_RIGHT]:
            self.x += self.vx

        if self.x <= 0:
            self.x = 0
        if self.x + self.rect.w >= self.padre.get_width():
            self.x = self.padre.get_width() - self.rect.w

class Bala():
    def __init__(self,padre, x, y):
        self.imagen = pg.image.load("./img/ball.png")
        self.rect = self.imagen.get_rect()
        self.padre = padre
        self.x = x
        self.y = y
        self.vy = 10
    
    def dibujar(self):
                
                self.padre.blit(self.imagen, (self.x, self.y))


    def mover(self):
        
        self.y -= self.vy
        
    def disparo(self):
        eventos = pg.event.get()
        for evento in eventos:
          if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        self.ball.x = self.nave.x
                        self.bala.y = self.nave.y -20
                        self.disparos.append(self.bala)
                        if len(self.disparos)> 1:
                            self.disparos.remove(self.bala)
            
        
            
                
class Game():
    def __init__(self, ancho = 900, alto = 700):
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.nave = Nave(self.pantalla, ancho //2, alto-80)
        self.reloj = pg.time.Clock()
        self.bala = Bala(self.pantalla, ancho//2, alto-110 )
        self.disparos= []
    
    
    
    
    
    
    
    def bucleppal(self):
        game_over = False
        disparo = False
        while not game_over:
            self.reloj.tick(60)
            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True
              
                        
                        
                        
                  
                        
                        
            
            
            self.pantalla.fill((255, 234, 123))
            
            self.bala.disparo()
            
            for element in self.disparos:
                
                element.mover()
                element.dibujar()
                    
            self.nave.mover()
            self.nave.dibujar()


            pg.display.flip()



if __name__ == "__main__":
    pg.init()
    game = Game()
    game.bucleppal()
    pg.quit()
    

