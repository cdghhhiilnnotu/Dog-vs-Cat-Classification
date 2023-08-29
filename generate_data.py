from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os
import numpy as np
import cv2

datagen = ImageDataGenerator(
    rotation_range=15, 
    rescale=1./255, 
    shear_range=0.1, 
    zoom_range=0.2, 
    horizontal_flip=True, 
    width_shift_range=0.1, 
    height_shift_range=0.1
)

dog_img = []
for filename in os.listdir('Data/train/dogs/'):
    pic = cv2.imread(f'Data/train/dogs/{filename}')
    pic_array = cv2.resize(pic, (28,28))
    dog_img.append(pic_array)

dog_img = np.array(dog_img)
count = 0
for batch in datagen.flow(dog_img, batch_size=2, save_to_dir='Data/train/dogs', save_prefix='dog.temp', save_format='png'):
    count += 1
    if count == 10:
        break

cat_img = []
for filename in os.listdir('Data/train/cats/'):
    # pic = load_img(f'Data/train/cats/{filename}')
    # pic_array = img_to_array(pic)
    pic = cv2.imread(f'Data/train/cats/{filename}')
    pic_array = cv2.resize(pic, (28,28))
    cat_img.append(pic_array)

cat_img = np.array(cat_img)
count = 0
for batch in datagen.flow(cat_img, batch_size=2, save_to_dir='Data/train/cats', save_prefix='cat.temp', save_format='png'):
    count += 1
    if count == 10:
        break

