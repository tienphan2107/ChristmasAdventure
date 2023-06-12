import random
import sys
import pygame

from button import Button
from setting import *
from tile import *
pygame.init()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.onMusic = True
        self.onOrOff = 3
        self.onOrOffBgGame = 3
        self.onMusicBgGame = True
        pygame.mixer.music.load('audio/Jingle Bells - Kevin MacLeod.mp3')
        pygame.mixer.music.set_volume(0.1)
        self.current_menu = None

    def create_menu(self):
        if self.current_menu is not None:
            pygame.display.quit()  # tắt cửa sổ hiện

        # pygame.mixer.music.play(-1)
        self.offMusic()
        # background_menu = pygame.image.load("graphics/background/background_menu_2.png")
        background_menu = pygame.image.load("graphics/background/background_bg.png")
        pygame.display.set_caption("Menu")

        while True:
            self.screen.blit(background_menu, (0, 0))
            # self.offMusic()
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            MENU_TEXT = self.get_font(34).render("SANTA'S CHRISTMAS EVE ADVENTURE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(620, 120))
            PLAY_BUTTON = Button(image=pygame.image.load("graphics/menu/Play Rectq.png"), pos=(620, 350),
                                 text_input="PLAY", font=self.get_font(25), base_color="#1F697D", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("graphics/menu/Options Rectq.png"), pos=(620, 450),
                                    text_input="OPTIONS", font=self.get_font(25), base_color="#1F697D",
                                    hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 550),
                                 text_input="QUIT", font=self.get_font(25), base_color="#1F697D", hovering_color="White")

            self.screen.blit(MENU_TEXT, MENU_RECT)
            for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        return self.onMusicBgGame

                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.show_options_screen(self.onOrOff, self.onOrOffBgGame)
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()


    def pause_menu(self, screen):

        RESUME_BUTTON = Button(image=pygame.image.load("graphics/menu/Play Rectq.png"), pos=(620, 250),
                             text_input="RESUME", font=self.get_font(25), base_color="#008DB9", hovering_color="WHITE")

        REPLAY_BUTTON = Button(image=pygame.image.load("graphics/menu/Options Rectq.png"), pos=(620, 350),
                                text_input="REPLAY", font=self.get_font(25), base_color="#008DB9",
                                hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 550),
                             text_input="QUIT", font=self.get_font(25), base_color="#008DB9", hovering_color="WHITE")

        MENU_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 450),
                             text_input="MENU", font=self.get_font(25), base_color="#008DB9", hovering_color="WHITE")

        # Hiển thị menu
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Kiểm tra xem người dùng có nhấp chuột không
            if pygame.mouse.get_pressed()[0]:
                # Kiểm tra xem vị trí chuột có nằm trong resume_rect không
                if RESUME_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Tiếp tục chơi
                    return "resume"

                # Kiểm tra xem vị trí chuột có nằm trong replay_rect không
                elif REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Chơi lại từ đầu
                    return "replay"

                # Kiểm tra xem vị trí chuột có nằm trong quit_rect không
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Thoát trò chơi
                    return "quit"

                elif MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Thoát trò chơi
                    return "menu"

            for button in [RESUME_BUTTON ,REPLAY_BUTTON, QUIT_BUTTON, MENU_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            pygame.display.update()

    def gameover_menu(self, screen):

        # Hiển thị Game Over và nút Replay
        font_menu = pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", 70)
        gameover_text = font_menu.render("Game Over", True, (168, 21, 11))
        gameover_rect = gameover_text.get_rect(center=(screen_width // 2, screen_height // 2 - 120))

        REPLAY_BUTTON = Button(image=pygame.image.load("graphics/menu/Options Rectq.png"), pos=(620, 400),
                               text_input="REPLAY", font=self.get_font(25), base_color="#008DB9",
                               hovering_color="WHITE")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 600),
                             text_input="QUIT", font=self.get_font(25), base_color="#008DB9", hovering_color="WHITE")

        MENU_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 500),
                             text_input="MENU", font=self.get_font(25), base_color="#008DB9", hovering_color="WHITE")

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Lấy vị trí chuột
            mouse_pos = pygame.mouse.get_pos()

            # Kiểm tra xem người dùng có nhấp chuột không
            if pygame.mouse.get_pressed()[0]:
                # Kiểm tra xem vị trí chuột có nằm trong replay_rect không
                if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                # Chơi lại từ đầu
                    return "replay"
                # Kiểm tra xem vị trí chuột có nằm trong quit_rect không
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Thoát trò chơi
                    return "quit"
                elif MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Thoát trò chơi
                    return "menu"


            screen.blit(gameover_text, gameover_rect)

            for button in [REPLAY_BUTTON, QUIT_BUTTON, MENU_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            pygame.display.update()

    def win_menu(self, screen):

        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            font_menu = pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", 60)
            win_text = font_menu.render("Congratulations!", True, (168, 21, 11))
            win_rect = win_text.get_rect(center=(screen_width // 2, screen_height // 2 - 120))

            REPLAY_BUTTON = Button(image=pygame.image.load("graphics/menu/Options Rectq.png"), pos=(620, 400),
                                   text_input="REPLAY", font=self.get_font(25), base_color="#008DB9",
                                   hovering_color="WHITE")
            QUIT_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 600),
                                 text_input="QUIT", font=self.get_font(25), base_color="#008DB9",
                                 hovering_color="WHITE")
            MENU_BUTTON = Button(image=pygame.image.load("graphics/menu/Quit Rectq.png"), pos=(620, 500),
                                 text_input="MENU", font=self.get_font(25), base_color="#008DB9",
                                 hovering_color="WHITE")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            if pygame.mouse.get_pressed()[0]:
                # Kiểm tra xem vị trí chuột có nằm trong replay_rect không
                if REPLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                # Chơi lại từ đầu
                    return "replay"
                # Kiểm tra xem vị trí chuột có nằm trong quit_rect không
                elif QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Thoát trò chơi
                    return "quit"
                elif MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # Thoát trò chơi
                    return "menu"

            screen.blit(win_text, win_rect)

            for button in [REPLAY_BUTTON, QUIT_BUTTON, MENU_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.screen)

            pygame.display.update()

    def show_options_screen(self, onOrOff, onOrOffBgGame):

        # Load background image and set window caption
        options_bg = pygame.image.load("graphics/background/background_menu_2.png")
        pygame.display.set_caption("Options")

        # Create button to return to main menu
        BACK_BUTTON = Button(image=pygame.image.load("graphics/menu/Play Rectq.png"), pos=(125, 100),
                             text_input="BACK", font=self.get_font(25), base_color="#1F697D", hovering_color="White")

        # Loop to display options screen
        while True:
            self.screen.blit(options_bg, (0, 0))
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
            # Check for button interactions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if ONMUSIC_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        self.onOrOff = self.onOrOff + 1
                        if onOrOff % 2 == 0:
                            self.onMusic = True
                            self.create_menu()
                            return
                        else:
                            self.onMusic = False
                            self.create_menu()
                            return

                    elif ONMUSIC_BG_GAME_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        self.onOrOffBgGame = self.onOrOffBgGame + 1
                        if self.onOrOffBgGame % 2 == 0:
                            self.onMusicBgGame = False
                            # self.create_menu()
                            return
                        else:
                            self.onMusicBgGame = True
                            # self.create_menu()
                            return
                    elif BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                        return

            if onOrOff % 2 != 0:
                text_input = "OFF MUSIC MENU"
            else:
                text_input = "ON MUSIC MENU"

            if onOrOffBgGame % 2 != 0:
                text_inputBGGame = "OFF MUSIC GAME"
            else:
                text_inputBGGame = "ON MUSIC GAME"

            ONMUSIC_BUTTON = Button(image=pygame.image.load("graphics/menu/Options Rectq.png"), pos=(620, 450),
                                    text_input=text_input, font=self.get_font(25), base_color="#008DB9",
                                    hovering_color="WHITE")

            ONMUSIC_BG_GAME_BUTTON = Button(image=pygame.image.load("graphics/menu/Options Rectq.png"), pos=(620, 550),
                                            text_input=text_inputBGGame, font=self.get_font(25), base_color="#008DB9",
                                            hovering_color="WHITE")

            for button in [BACK_BUTTON, ONMUSIC_BUTTON, ONMUSIC_BG_GAME_BUTTON]:
                button.changeColor(OPTIONS_MOUSE_POS)
                button.update(self.screen)

            pygame.display.update()

    def get_font(self, size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font("fonts/Press_Start_2P/PressStart2P-Regular.ttf", size)

    def offMusic(self):
        if self.onMusic == True:
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()


