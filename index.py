from pygame import *
class GameSprite(sprite.Sprite):
  def __init__ (self, player_image, player_x, player_y, player_speed, width, height)
  self.image = transform.scale(image.load(player_image),(width,height))
  self.speed = player_speed
  self.rect = self.image.get_rect
  self.rect.x = player_x
  self.rect.y = player.y
class Player(GameSprite):
  def update_r(self):
    keys = key.get_pressed()
    if keys[K_UP] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_DOWN] and self.rect.y < win_height -80:
      self.rect.y += self.speed

  def update_l(self):
    keys = key.get_pressed()
    if keys[K_w] and self.rect.y > 5:
      self.rect.y -= self.speed
    if keys[K_s] and self.rect.y < win_height -80:
      self.rect.y += self.speed
back = (0,0,0)
win_width = 600
win_height = 500
window = display.set_mode((win_width,win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player(raket_genisligi = 100raket_yuksekligi = 20raket_rengi = (255, 255, 255) raket = pygame.Rect(window_genisligi / 2 - raket_genisligi / 2, window_yuksekligi - raket_yuksekligi - 20, raket_genisligi, raket_yuksekligi))

racket2 = Player(raket_genisligi = 100raket_yuksekligi = 20raket_rengi = (255, 255, 255) raket = pygame.Rect(window_genisligi / 2 - raket_genisligi / 2, window_yuksekligi - raket_yuksekligi - 20, raket_genisligi, raket_yuksekligi))
font.init()
font = font.Font(None,35)
lose1 = font.render("Player 1 lost!", True, (255,0,0))
lose2 = font.render("Player 2 lost!", True, (255,0,0))
speed_x = 3
speed_y = 3
