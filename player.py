import pygame
from support import import_folder
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()

        # cái này chuyển ảnh thành bề mặt lưu vào biến self.animation
        self.import_player_assets()
        self.frame_index = 0  # biến này sẽ chọn lấy ảnh thứ mấy trong 1 animation
        self.animation_speed = 0.15  # biến này sẽ tăng dần r chọn 1 ảnh tiếp theo

        self.image = pygame.Surface((32, 64))  # kích thước nhân vật
        self.image = self.animations['idle'][self.frame_index]  # chọn ảnh cho player

        self.rect = self.image.get_rect(topleft=pos)

        # biến này sẽ xác định hướng di chuyển của player
        self.direction = pygame.math.Vector2(0, 0)
        # di chuyển player
        self.speed = 8
        self.gravity = 0.8  # biến này là trọng lực kéo player xuống
        self.jump_speed = -16  # tại trục OY hướng xuống nên nhảy lên thì Y giảm

        # player mặc định lúc đầu
        self.status = 'idle'
        self.facing_right = True  # cái biến này cho biết đang nhìn hướng nào
        self.on_ground = False

        # Thanh Máu
        self.heart = Heart()
        self.invincible = False  # tình trạng nhấp nháy
        self.time_duration = 500  # khoảng cách 2 lần mất máu 500ms
        self.hurt_time = 0  # thời điểm bị thương

        # âm thanh
        #ouch
        self.get_damage_sound = pygame.mixer.Sound('audio/getdamagesound.mp3')
        #jump
        self.get_jump = pygame.mixer.Sound('audio/jump.wav')


    def import_player_assets(self):
        player_path = 'graphics/player/'  # chổ này đổi dường dẫn ------------------------------------------
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': []}
        for animation in self.animations.keys():
            full_path = player_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):  # hàm này thay đổi ảnh của nhân vật theo thời gian
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed  # 0.15 sẽ dc cộng dồn
        if self.frame_index > len(animation):  # index lớn hơn số ảnh đang có
            self.frame_index = 0
        image = animation[int(self.frame_index)]  # đổi ảnh player
        if (self.facing_right):  # xét xem hướng mặt player
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)  # xoay ảnh (tênBien, Trục X, Trục Y)

        # Nhấp nháy
        if self.invincible:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def get_status(self):
        x = self.direction.x  # x,y là trạng thái di chuyển của player
        y = self.direction.y
        if x != 0 and y == 0:
            self.status = 'run'
        elif y < 0:
            self.status = 'jump'
        elif y > 1:  # vì Y nó lúc nào cũng là 0,8 do có trọng lực
            self.status = 'fall'
        else:
            self.status = 'idle'

    def input(self):  # hàm này nhận thao tác từ phím
        input = pygame.key.get_pressed()
        if input[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif input[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if input[pygame.K_SPACE]:
            self.jump()
            self.on_ground = False;

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        if (self.on_ground):
            self.direction.y = self.jump_speed
            self.get_jump.play()  # kêu ouch khi mất máu

    def get_damage(self):
        if not self.invincible:
            self.get_damage_sound.play()  # kêu ouch khi mất máu
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()
            self.heart.update(-1)

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.time_duration:
                self.invincible = False

    def wave_value(self):
        value = math.sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

    def update(self):
        self.input()
        self.get_status()
        self.animate()
        self.invincibility_timer()


class Heart:
    def __init__(self):
        self.total = 5  # số máu hiện có
        self.image = pygame.surface.Surface((32, 32))
        self.image = pygame.image.load('graphics/heart/heart.png')
        # heart_font = pygame.font.SysFont('Arial', 32)
        # heart_text = heart_font.render(str('self.total'), True, (255, 255, 255), (0, 0, 0))
        # self.image.blit(heart_text, (42, 10))
        self.rect = self.image.get_rect(topleft=(10, 10))

    def draw(self, surface):  # hàm này vẽ ra số trái tim tương ứng
        for i in range(self.total):
            surface.blit(self.image, self.rect)
            self.rect.x += 42  # mỗi trái tim rộng 32 cách nhau 10 nên cái rect tăng thêm 42
        self.rect.x = 10  # cố định cái rect lại để mấy trái tim nó bay khỏi màn hình á

    def update(self, number):
        self.total += number
