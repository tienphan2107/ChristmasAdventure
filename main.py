
import sys
import pygame

from menu import Menu
from setting import *
from tile import *
from level import *
from pygame.image import load

pygame.init()

main_screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
current_menu = None

#khởi tạo con chuột
surf = load('graphics/cursor/mouse.png').convert_alpha()
cursor = pygame.cursors.Cursor((0,0), surf)
pygame.mouse.set_cursor(cursor)

# Tạo đối tượng menu
menu = Menu(main_screen)

# Gọi hàm vẽ menu
music = menu.create_menu()


# Tạo background và level
background_image = pygame.image.load('graphics/background/background.png').convert_alpha()
level = Level(map, main_screen)

# Tạo âm thanh game
# pygame.mixer.music.load('audio/Jingle Bells 7 - Kevin MacLeod.mp3')
# pygame.mixer.music.set_volume(0.1)
# pygame.mixer.music.play(-1)

def offMusicbggame():
    # if menu.onMusicBgGame == True:
    #     pygame.mixer.music.play(-1)
    # elif menu.onMusicBgGame == False:
    #     pygame.mixer.music.stop()
    if music == True:
        level.level_music()
    elif music == False:
        level.level_music_off()

offMusicbggame()

# Tạo biến boolean để kiểm tra trạng thái tạm dừng của trò chơi
paused = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # Nếu trạng thái là đang chạy, đặt thành tạm dừng và hiển thị menu tạm dừng
                if not paused:
                    paused = True
                    menu_choice = menu.pause_menu(main_screen)
                    if menu_choice == "resume":
                        paused = False
                    elif menu_choice == "quit":
                        pygame.quit()
                        sys.exit()
                    elif menu_choice == "replay":
                        paused = False

                        level = Level(map, main_screen)  # truyền vào map_data và main_screen khi khởi tạo Level
                        # Chạy trò chơi từ đầu
                        main_screen.fill('black')
                        main_screen.blit(background_image, (0, 0))
                        level.run()
                        pygame.display.update()
                        clock.tick(60)

                    elif menu_choice == "menu":
                        paused = False

                        if current_menu is not None:
                            pygame.display.quit()  # tắt cửa sổ hiện
                        # Chạy trò chơi từ đầu
                        main_screen.fill('black')
                        main_screen.blit(background_image, (0, 0))
                        menu1 = Menu(main_screen)
                        menu1.create_menu()
                        level = Level(map, main_screen)  # truyền vào map_data và main_screen khi khởi tạo Level
                        level.run()
                        pygame.display.update()
                        clock.tick(60)
                # Nếu trạng thái là đang tạm dừng, đặt lại thành đang chạy
                else:
                    paused = False

    # Nếu trạng thái là đang chạy, tiếp tục chơi
    if not paused:
        main_screen.fill('black')
        main_screen.blit(background_image, (0, 0))
        level.run()
        pygame.display.update()
        clock.tick(60)

    # kiểm tra gameover từ out_of_map() hoặc là out_health
        if level.check_gameover():
            menu.gameover_menu(main_screen)
            menu_choice_gameover = menu.gameover_menu(main_screen)
            if menu_choice_gameover == 'quit':
                pygame.quit()
                sys.exit()
            elif menu_choice_gameover == 'replay':
                level = Level(map, main_screen)  # truyền vào map_data và main_screen khi khởi tạo Level
                paused = False
                # Chạy trò chơi từ đầu

                main_screen.fill('black')
                main_screen.blit(background_image, (0, 0))
                level.run()
                pygame.display.update()
                clock.tick(60)
            elif menu_choice_gameover == "menu":
                paused = False
                # Chạy trò chơi từ đầu
                if current_menu is not None:
                    pygame.display.quit()  # tắt cửa sổ hiện
                main_screen.fill('black')
                main_screen.blit(background_image, (0, 0))
                menu1 = Menu(main_screen)
                menu1.create_menu()
                level = Level(map, main_screen)  # truyền vào map_data và main_screen khi khởi tạo Level
                level.run()
                pygame.display.update()
                clock.tick(60)
        if level.check_win():
            menu.win_menu(main_screen)
            menu_choice_win = menu.win_menu(main_screen)
            if menu_choice_win == 'quit':
                pygame.quit()
                sys.exit()
            elif menu_choice_win == 'replay':
                level = Level(map, main_screen)  # truyền vào map_data và main_screen khi khởi tạo Level
                paused = False
                # Chạy trò chơi từ đầu
                main_screen.fill('black')
                main_screen.blit(background_image, (0, 0))
                level.run()
                pygame.display.update()
                clock.tick(60)
            elif menu_choice_win == "menu":
                paused = False
                if current_menu is not None:
                    pygame.display.quit()  # tắt cửa sổ hiện
                # Chạy trò chơi từ đầu
                main_screen.fill('black')
                main_screen.blit(background_image, (0, 0))
                menu1 = Menu(main_screen)
                menu1.create_menu()
                level = Level(map, main_screen)  # truyền vào map_data và main_screen khi khởi tạo Level
                level.run()
                pygame.display.update()
                clock.tick(60)