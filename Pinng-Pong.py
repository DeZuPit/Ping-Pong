from pygame import *

finish = False
run = True

app = QApplication([])
see = QWidget()
see.setWindowTitle('Умные заметки')
see.resize(900, 600)

img_stena = 

class GameSprite(sprite.Sprite):
     
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       
        sprite.Sprite.__init__(self)
 
     
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
 
      
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
     
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x:
            self.rect.x += self.speed
        if keys[K_DOWN] and self.rect.x:
            self.rect.x -= self.speed