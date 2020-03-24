import pygame

window_width= 965
window_height= 480
red= (255, 0,0)
green= (0, 100, 0)
black = (0,0,0)

class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x=x
        self.y=y
        self.width=width
        self.height=height

        #makes a rectangle around the entity 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

class Bomb(Entity):
    def __init__(self,  x, y, width, height):
        super().__init__(x, y, width, height)

        self.image= pygame.Surface([self.width, self.height])
        entity_color=black
        self.image.fill(entity_color)

        #set speed
        self.x_change= 0
        self.y_change= 10

    def update(self):
        #moves it relative to current location
        self.rect.move_ip(self.x_change, self.y_change)


class Plane(Entity):
    def __init__(self,  x, y, width, height):
        super().__init__(x, y, width, height)

        self.image= pygame.Surface([self.width, self.height])
        entity_color=red
        self.image.fill(entity_color)

        #set plane speed
        self.x_change= 9
        self.y_change= 0

    def speed_up(self):
        if self.x_change< 0:
            self.x_change-=1
        elif self.x_change > 0:
            self.x_change += 1

    def update(self):
        #moves plane and makes sure it stays in bounds

        #prevents moves off screen
        if self.rect.x < 0 or self.rect.x > window_width - self.width:
            self.x_change *= -1

        #moves it relative to current location
        self.rect.move_ip(self.x_change, self.y_change)



class Tank(Entity):
    def __init__(self,  x, y, width, height, x_change):
        super().__init__(x, y, width, height)

        self.image= pygame.Surface([self.width, self.height])
        entity_color=green
        self.image.fill(entity_color)

        #set tank speed
        self.x_change= x_change
        self.y_change= 0

    def update(self):
        #moves tank 

        #moves it relative to current location
        self.rect.move_ip(self.x_change, self.y_change)




