from pygame import *
from random import randint
from time import time as timer #импортируем функцию для засекания времени, чтобы интерпретатор не искал эту функцию в pygame модуле time, даём ей другое название сами
#подгружаем отдельно функции для работы со шрифтом
font.init()
font1 = font.SysFont(None, 80)
win = font1.render('PLAYER 1 WIN', True, (255, 255, 255))
lose = font1.render('PLAYER 2 WIN', True, (180, 0, 0))
#нам нужны такие картинки:
img_back =  (200,100,200)
score = 0 #сбито кораблей
goal = 20 #столько кораблей нужно сбить для победы
lost = 0 #пропущено кораблей
max_lost = 10 #проиграли, если пропустили столько кораблей
life = 3  #очки жизни
img_myach = "asteroid.png"
img_platform = "platform.webp"
run = True
finish = False
win_width = 700
win_height = 500
display.set_caption("PingPong")
window = display.set_mode((win_width, win_height))
#класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
#конструктор класса 
  def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #вызываем конструктор класса (Sprite):
      sprite.Sprite.__init__(self)
      #каждый спрайт должен хранить свойство image - изображение
      self.image = transform.scale(image.load(player_image), (size_x, size_y))
      self.speed = player_speed
      #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#метод, отрисовывающий героя на окне
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#класс главного игрока
class Player(GameSprite):
  #метод для управления спрайтом стрелками клавиатуры
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_width - 80:
            self.rect.y += self.speed
        
    def updates(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 600:
            self.rect.y += self.speed

myach = Player(img_myach, 300, 330, 80, 50, 4)
platform1 = Player(img_platform, 30, 200, 10, 120, 12)
platform2 = Player(img_platform, 650, 200, 10, 120, 12)
while run:
  #событие нажатия на кнопку “Закрыть”
  for e in event.get():
      if e.type == QUIT:
        run = False
        
  if not finish:
    window.fill(img_back)
    myach.reset()
    platform1.reset()
    platform2.reset()
    platform1.update()
    platform2.updates()
    display.update()

  time.delay(50)
