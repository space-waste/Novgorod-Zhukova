import os, random
import pygame

pygame.init()

FPS = 8
WIDTH = 1200
HEIGHT = 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
y = 392
x = 500
all_sprites = pygame.sprite.Group()
meteor1 = pygame.sprite.Group()


def start_screen():
    intro_text = ["",
                  "",
                  "вы здохли",
                  "",
                  ""]

    fon = pygame.transform.scale(load_image('Mori.png'), (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 150)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if dragon.rect.left > 0:
                l = 7
                dragon.image = pygame.transform.flip(dragon.image, True, False)
                dragon.rect.left -= l
        if key[pygame.K_RIGHT]:
            if dragon.rect.left < 1110:
                r = 7
                dragon.rect.left += r
        meteor.rect.left += vpavo
        meteor.rect.top += vniz
        meteor2.rect.left += vpavo2
        meteor2.rect.top += vniz2


class Dino(AnimatedSprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(sheet, columns, rows, x, y)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)


class Meteor(AnimatedSprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(sheet, columns, rows, x, y)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)


dragon = Dino(load_image("dino.png", color_key=(255, 0, 0)), 6, 1, 500, 392)

y = random.randrange(WIDTH - 100)
meteor = Meteor(load_image("meteor.png", color_key=(0, 0, 255)), 4, 1, y, 0)
# pygame.sprite.mask = pygame.mask.from_surface(pygame.sprite.meteor)
vniz = random.randrange(5, 30)
vpavo = random.randrange(5, 15)
meteor1.add(meteor)
y = random.randrange(WIDTH - 100)
meteor2 = Meteor(load_image("meteor.png", color_key=(0, 0, 255)), 4, 1, y, 0)
# pygame.sprite.mask = pygame.mask.from_surface(pygame.sprite.meteor)
vniz2 = random.randrange(10, 30)
vpavo2 = random.randrange(5, 15)
meteor1.add(meteor2)
sprite = pygame.sprite.Sprite(all_sprites)
sprite.image = load_image("earth.png", color_key=(255, 0, 0))
sprite.rect = sprite.image.get_rect()

sprite.rect.x = 0
sprite.rect.y = 474
all_sprites.add(sprite)

running = True
q = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        key = pygame.key.get_pressed()
    q += 1
    if q % 10 == 2 and q > 20:
        meteor.rect.x = random.randrange(WIDTH - 100)
        meteor.rect.y = 0
    if q % 22 == 15 and q > 30:
        meteor2.rect.x = random.randrange(WIDTH - 100)
        meteor2.rect.y = 0
    # if pygame.sprite.spritecollideany(dragon, meteor1):
    # dragon = AnimatedSprite(load_image('dino_l.png', color_key=(255, 0, 0)), 6, 1, 500, 392)
    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    all_sprites.update()
    meteor1.update()
    if pygame.sprite.spritecollideany(dragon, meteor1):
        start_screen()
        running = False
    pygame.display.flip()

    clock.tick(FPS)

start_screen()
start_screen()
start_screen()
start_screen()
start_screen()
start_screen()
start_screen()
start_screen()
start_screen()
start_screen()
pygame.display.flip()
pygame.quit()
