from os import walk  # walk giúp ta di chuyển giữa các file trong các folder
import pygame

# walk trả về 3 tuple: tên đường dẫn (path), tên các tệp con trong đường dẫn đó, dsach các file con của đường dẫn

def import_folder(path):  # hàm này truy cập đường dẫn và tạo 1 danh sách các bề mặt từ các ảnh trong đó

    surface_list = []
    for _, __, image_file in walk(path):  # duyệt từ thư mục gốc (path), ta không cần 2 giá trị đầu của hàm walk
        for image in image_file:
            full_path = path + '/' + image
            image_surface = pygame.image.load(full_path).convert_alpha()  # tạo bản sao để tăng độ mờ
            surface_list.append(image_surface)

    return surface_list

