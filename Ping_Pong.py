from pygame import *

class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_Left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
    def update_Right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_width - 80:
            self.rect.y += self.speed

Indigo = (75, 0, 130)
win_width = 600
win_height = 500
display.set_caption("Shooter")
window = display.set_mode((win_width, win_height))

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 lose', True, (200, 0, 0))
lose2 = font.render('Player 2 lose', True, (200, 0, 0))

r_image = 'r.png'
speed = 5
height = 150
width = 50

speed_x = 3
speed_y = 3

finish = False
run = True
clock = time.Clock()
FPS = 60
r1 = Player(r_image, 30, 200, width, height, speed)
r2 = Player(r_image, 520, 200, width, height, speed)
ball = GameSprite('ball.png', 200, 200, 50, 50, speed)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if finish != True:

        window.fill(Indigo)
        r1.update_Left()
        r2.update_Right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        r1.reset()
        r2.reset()
        ball.reset()

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            speed_y *= -1
            
        if sprite.collide_rect(r1, ball) or sprite.collide_rect(r2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            window.blit(lose1, (200, 200))
            finish = True

        if ball.rect.x > win_width:
            window.blit(lose2, (200, 200))
            finish = True

        display.update()
        clock.tick(FPS)


