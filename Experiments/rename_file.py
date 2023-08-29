# import keras
# import cv2
# import numpy as np

# Khai báo thư viện os
import os

# Đánh số thứ tự của ảnh
i = 0
# Lấy địa chỉ thư mục chứa ảnh
path2="Data/img/"
# Lặp qua các ảnh trong địa chỉ thư mục vừa lấy
for filename in os.listdir(path2):
    # Đặt tên mới cho ảnh
    my_dest ="cat." + str(i) + ".jpg"
    # Lấy địa chỉ của ảnh: Data/img/ + dogs.0.jpg = Data/img/dogs.0.jpg
    my_source = path2 + filename
    # Tạo địa chỉ mới cho ảnh: Data/img/ + cat.0.jpg = Data/img/cat.0.jpg
    my_dest = path2 + my_dest
    # Thực hiện việc thay đổi tên
    os.rename(my_source, my_dest)
    # Tăng số thứ tự
    i += 1












