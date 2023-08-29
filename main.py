# # import Experiments.convert_data as convert_data
import cv2
import os
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Dropout, BatchNormalization
import random
import math

# data_X, data_Y = convert_data.Get_Data().getData()

# X_train, X_test = data_X[:math.ceil(0.7 * data_X.shape[0])], data_X[math.ceil(0.7 * data_X.shape[0]):]
# Y_train, Y_test = data_Y[:math.ceil(0.7 * data_Y.shape[0])], data_Y[math.ceil(0.7 * data_Y.shape[0]):]

cat_dir = 'Data/train/cats'
dog_dir = 'Data/train/dogs'

list_dog = []
list_cat = []
list_ani = []

data = []
x_train = []
y_train = []
for filename in os.listdir(cat_dir):
    file = os.path.join(cat_dir, filename)
    list_cat.append(file)
    list_ani.append(file)

for filename in os.listdir(dog_dir):
    file = os.path.join(dog_dir, filename)
    list_dog.append(file)
    list_ani.append(file)

random.shuffle(list_ani)

for file in list_ani:
    img = cv2.imread(file)
    img = cv2.resize(img, (28,28))
    x_train.append(img)
    if file in list_cat:
        y_train.append([0, 1])
    elif file in list_dog:
        y_train.append([1, 0])

x_data = np.array(x_train)
y_data = np.array(y_train)
X_train, X_test = x_data[:math.ceil(0.7 * x_data.shape[0])], x_data[math.ceil(0.7 * x_data.shape[0]):]
Y_train, Y_test = y_data[:math.ceil(0.7 * y_data.shape[0])], y_data[math.ceil(0.7 * y_data.shape[0]):]

model = Sequential()

model.add(Conv2D(32, kernel_size=(3,3), padding='valid', activation='relu', input_shape=(28, 28, 3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

model.add(Conv2D(64, kernel_size=(3,3), padding='valid', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

model.add(Conv2D(128, kernel_size=(3,3), padding='valid', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2), strides=2, padding='valid'))

model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(2))

model.compile(
    loss=keras.losses.BinaryCrossentropy(from_logits=True),
    optimizer=keras.optimizers.Adam(lr=0.01),
    metrics=['accuracy']
)

model.fit(X_train, Y_train, batch_size=64, epochs=5, verbose=1)
model.evaluate(X_test, Y_test, batch_size=64, verbose=1)

model.save('model-1.keras')


