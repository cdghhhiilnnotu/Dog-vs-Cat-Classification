import keras
import matplotlib.pyplot as plt
import cv2
import os
import random
import numpy as np

imgTest = 1
classes = ['Dog', 'Cat']

class_list = os.listdir('Data/test')
idxclass = random.randrange(0,2)
img_list = os.listdir(f'Data/test/{class_list[idxclass]}')
idximg = random.randrange(0,len(img_list))
img = cv2.imread(f'Data/test/{class_list[idxclass]}/{img_list[idximg]}')
img2 = cv2.resize(img, (28,28))

img_arr = img2.reshape((1,) + img2.shape)

model = keras.models.load_model('model-1.keras')
prediction = model.predict(img_arr)

plt.imshow(img)
plt.xlabel(f'Predictions: {classes[np.argmax(prediction)]}')
plt.show()



