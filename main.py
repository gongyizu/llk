import pygame
from os import path
from base import (
    data,
    isZeroTurnLinked,
    isOneTurnLinked,
    isTwoTurnLinked,
    Point,
    gen_data,
)

gen_data()
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 1100
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ROLE_SIZE = 75

matching_pair = []


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("连连看")
FPS = 60
clock = pygame.time.Clock()
showline = (None, None, None, None)
draw_line_time = 0

img_dir = path.join(path.dirname(__file__), "images", "100")
snd_dir = path.join(path.dirname(__file__), "sounds")

snd_clear = pygame.mixer.Sound(path.join(snd_dir, "clear.ogg"))


class Pokemon(pygame.sprite.Sprite):
    def __init__(self, idx, row, col, callback):
        pygame.sprite.Sprite.__init__(self)

        imgName = f"{idx}.jpg"
        if idx < 10:
            imgName = f"0{idx}.jpg"

        converted_img = pygame.image.load(path.join(img_dir, imgName)).convert()
        self.image = pygame.transform.scale(converted_img, (ROLE_SIZE, ROLE_SIZE))
        pygame.draw.rect(self.image, BLUE, self.image.get_rect(), 2)
        # self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = col * ROLE_SIZE + ROLE_SIZE / 2
        self.rect.centery = row * ROLE_SIZE + ROLE_SIZE / 2
        self.idx = idx
        self.callback = callback
        self.point = Point(col, row)
        self.selected = False

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.callback(self)

    def toggle_selected(self):
        self.selected = not self.selected
        border_color = BLUE

        if self.selected:
            border_color = RED
        pygame.draw.rect(self.image, border_color, self.image.get_rect(), 2)


pokemons = pygame.sprite.Group()


def check_status():
    """
    TODO: 检查是否无解局
    """
    pass


def trigger_matched(pkm1, pkm2, pt1=None, pt2=None):
    global showline
    # 连线
    showline = (pkm1.point, pkm2.point, pt1, pt2)

    # 修改数组
    data[pkm1.point.y][pkm1.point.x] = 0
    data[pkm2.point.y][pkm2.point.x] = 0
    # 删除角色
    pkm1.kill()
    pkm2.kill()
    matching_pair.clear()
    # 检查是否死局
    check_status()


def pkm_clicked(sprite):
    """
    角色被点击
    """
    matching_len = len(matching_pair)
    if matching_len == 0:
        sprite.toggle_selected()
        matching_pair.append(sprite)
    elif matching_len == 1:
        sprite.toggle_selected()
        matching_pair.append(sprite)

        p0 = matching_pair[0]
        p1 = matching_pair[1]

        if (
            not (p0.point.x == p1.point.x and p0.point.y == p1.point.y)
        ) and p0.idx == p1.idx:
            matched = isZeroTurnLinked(p0.point, p1.point)
            if matched:
                trigger_matched(p0, p1)
                return

            (matched, tmpPoint) = isOneTurnLinked(p0.point, p1.point)
            if matched:
                trigger_matched(p0, p1, tmpPoint)
                return

            (matched, tmpPoint1, tmpPoint2) = isTwoTurnLinked(p0.point, p1.point)
            if matched:
                trigger_matched(p0, p1, tmpPoint1, tmpPoint2)
                return

        p0.toggle_selected()
        p1.toggle_selected()
        matching_pair.clear()
    elif matching_len == 2:
        # 原先选中的两张图片取消选中状态
        matching_pair[0].toggle_selected()
        matching_pair[1].toggle_selected()
        matching_pair.clear()


def draw_line(point1, point2):
    """
    画连接线
    """
    pygame.draw.line(
        screen,
        RED,
        (
            point1.x * ROLE_SIZE + ROLE_SIZE / 2,
            point1.y * ROLE_SIZE + ROLE_SIZE / 2,
        ),
        (
            point2.x * ROLE_SIZE + ROLE_SIZE / 2,
            point2.y * ROLE_SIZE + ROLE_SIZE / 2,
        ),
        5,
    )


# 遍历数组，生成图阵
for i in range(len(data)):
    row = data[i]
    for j in range(len(row)):
        item = row[j]
        if item > 0:
            pkm = Pokemon(item, i, j, pkm_clicked)
            pokemons.add(pkm)

running = True
while running:
    clock.tick(FPS)
    events = pygame.event.get()
    for evt in events:
        if evt.type == pygame.QUIT:
            running = False

    pokemons.update(events)
    screen.fill(BLACK)
    pokemons.draw(screen)

    if showline[0] is not None:
        # 画出连接线
        if draw_line_time == 0:
            snd_clear.play()
            # 线条需要做短暂的视觉停留，第一次绘制的时候，记录时间
            draw_line_time = pygame.time.get_ticks()

        if showline[3] is not None:
            # 四点三线
            draw_line(showline[0], showline[2])
            draw_line(showline[2], showline[3])
            draw_line(showline[3], showline[1])
        elif showline[2] is not None:
            # 三个点两线
            draw_line(showline[0], showline[2])
            draw_line(showline[2], showline[1])
        else:
            # 两点一线
            draw_line(showline[0], showline[1])

    if (
        draw_line_time > 0
        and showline[0] is not None
        and pygame.time.get_ticks() - draw_line_time > 100
    ):
        # 清除连接线
        showline = (None, None, None, None)
        draw_line_time = 0

    pygame.display.flip()

pygame.quit()
