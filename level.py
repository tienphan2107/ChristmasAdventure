import random
import sys

import pygame
from pygame import time

from menu import Menu
from tile import *
from setting import *
from player import *
from gift import Gift
from trap import Trap
from decorate import Decorate

class Level():
    def __init__(self, map_data, surface):
        self.surface = surface
        self.map = self.setup_map(map_data)
        self.scroll_speed = 0  # tốc độ di chuyển của màn hình khi đi hết map
        # nhạc game
        self.game_play_sound = pygame.mixer.Sound('audio/Jingle Bells 7 - Kevin MacLeod.mp3')
        self.game_play_sound.set_volume(0.1)  # âm lượng 1 nửa

        self.menu = Menu(surface)
        self.checkwin = False

    def setup_map(self, map_data):
        self.tiles = pygame.sprite.Group()  # cái group này để lưu các block
        self.player = pygame.sprite.GroupSingle()  # cái group này để lưu 1 player
        self.gift = pygame.sprite.GroupSingle()  # lưu cái hộp quà
        self.traps = pygame.sprite.Group()  # lưu mấy cái bẫy
        self.decorates = pygame.sprite.Group()  # lưu mấy cái trang trí
        # khúc dưới duyệt mảng 2 chiều để vẽ map
        for row_index, row in enumerate(map_data):
            for col_index, col in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if col == '1' or col == '2' or col == '3' or col == '4' or col == '5' or col == '6':  # các index của block
                    tile = Tile((x, y), tile_size, col)
                    self.tiles.add(tile)
                elif col == '7' or col == '8' or col == '9' or col == '0':  # index mấy cái trang trí
                    decorate = Decorate((x, y), tile_size, col)
                    self.decorates.add(decorate)
                elif col == 'P':
                    self.player.add(Player((x, y)))
                elif col == 'G':
                    self.gift.add(Gift((x, y), tile_size))
                elif col == 'T':
                    y += 32
                    self.traps.add(Trap((x, y), tile_size))

    def scroll_map(self):
        player = self.player.sprite  # nhân vật
        player_x = player.rect.centerx  # tọa độ x của nhân vật
        direction_x = player.direction.x  # hướng đi của nhân vật

        if player_x < screen_width / 4 and direction_x < 0:  # đi tới x = 300 thì map cuộn qua trái
            player.speed = 0
            self.scroll_speed = 8
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:  # đi tới x = 900  thì map cuộn qua phải
            player.speed = 0
            self.scroll_speed = -8
        else:
            player.speed = 8
            self.scroll_speed = 0

    def horizontal_collision(self):  # va chạm khi đi ngang
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        gift = self.gift.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):  # hàm colliderect kiểm tra 2 rect có chạm nhau k
                if player.direction.x < 0:  # nếu đang qua trái mà va chạm thì sẽ reset cạnh phải nhân vật = cạnh phải vật thể -> k đi dc
                    player.rect.left = sprite.rect.right
                if player.direction.x > 0:
                    player.rect.right = sprite.rect.left  # nếu đang qua phải mà va chạm thì sẽ reset cạnh trái nhân vật = cạnh phải vật thể -> k đi dc

        for sprite in self.traps.sprites():
            if sprite.rect.colliderect(player.rect):  # hàm colliderect kiểm tra 2 rect có chạm nhau k
                player.get_damage()
                # if player.direction.x < 0:
                #     player.rect.left += 64
                #     player.image.set_alpha(50)
                # if player.direction.x > 0:
                #     player.rect.right -= 64

        if player.rect.colliderect(gift.rect):  # end game nếu chạm vào hộp quà
            self.checkwin = True

    def vertical_collision(self):  # va chạm khi lên xuống
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):  # hàm colliderect kiểm tra 2 rect có chạm nhau k
                if player.direction.y > 0 and player.rect.bottom >= sprite.rect.top:  # nếu đang xuống mà va chạm thì sẽ reset cạnh dưới nhân vật = cạnh trên vật thể -> k đi dc
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0  # reset lại để gravity cứ tăng hoài
                    player.on_ground = True
                if player.direction.y < 0 and player.rect.top <= sprite.rect.bottom:
                    player.rect.top = sprite.rect.bottom  # nếu đang lên mà va chạm thì sẽ reset cạnh trên nhân vật = cạnh dưới vật thể -> k đi dc
                    player.direction.y = 0
                    player.on_ground = False

        for sprite in self.traps.sprites():
            if sprite.rect.colliderect(player.rect):  # hàm colliderect kiểm tra 2 rect có chạm nhau k
                player.get_damage()
                # player.rect.bottom -= 64
                # if player.direction.x < 0:
                #     player.rect.left += 64
                # if player.direction.x > 0:
                #     player.rect.right -= 64

    def out_of_map(self):  # rớt xuống overworld
        player = self.player.sprite
        if player.rect.centery > 1000:
            return 1

    def out_of_heart(self):
        heart = self.player.sprite.heart
        if heart.total <= 0:
            return 1

    def run(self):
        self.tiles.update(self.scroll_speed)  # cái biến này là tốc độ trượt của map khi đi đến cuôi
        self.gift.sprite.update(self.scroll_speed)
        self.traps.update(self.scroll_speed)
        self.decorates.update(self.scroll_speed)

        self.decorates.draw(self.surface)  # vẽ mấy cái trang trí trước
        self.tiles.draw(self.surface)  # vẽ cái group gồm các sprite là các ô
        self.scroll_map()

        self.player.draw(self.surface)  # vẽ nhân vật
        self.player.sprite.heart.draw(self.surface)  # vẽ thanh máu
        self.player.update()  # bắt sự di chuyển của nhân vật
        self.horizontal_collision()
        self.vertical_collision()

        self.gift.draw(self.surface)
        self.traps.draw(self.surface)
        # kiểm tra end game
        self.out_of_map()
        self.out_of_heart()

        # phát nhạc với vòng lặp vô tận


    def check_gameover(self):
       if self.out_of_map() == 1:
           return True
       if self.out_of_heart() == 1:
           return True

    def check_win(self):
        if self.checkwin == True:
            return True

    def level_music(self):
        self.game_play_sound.play(-1)

    def level_music_off(self):
        self.game_play_sound.stop()
