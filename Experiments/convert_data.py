import cv2
import os
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Dropout, BatchNormalization
import random
import matplotlib.pyplot as plt

class Get_Data():
    def __init__(self):
        self.listXData = []
        self.listYData = []
        self.class0 = []
        self.class1 = []

    def readImg(self,imgPath):
        img = cv2.imread(imgPath)
        img = cv2.resize(img, (28,28))
        img = img/255.
        return img
    
    def isEqualImgs(self, img1, img2):
        compare = img1 == img2
        return compare.all()

    def numpyData(self, dirPath, classImg):
        listTemp = os.listdir(dirPath)
        for img in listTemp:
            imgPath = f'{dirPath}/{img}'
            imgArr = self.readImg(imgPath)
            self.listXData.append(imgArr)
            if classImg == 0:
                self.class0.append(imgArr)
            if classImg == 1:
                self.class1.append(imgArr)

    def inList0(self, img):
        for img0 in self.class0:
            if self.isEqualImgs(img0, img):
                return True
        return False
    
    def inList1(self, img):
        for img1 in self.class1:
            if self.isEqualImgs(img1, img):
                return True
        return False

    def labelData(self):
        for data in self.listXData:
            if self.inList0(data):
                self.listYData.append(0)
            if self.inList1(data):
                self.listYData.append(1)

    def getData(self):
        # for i in range(2):
        self.numpyData(f'Data1/train/dogs', 0)
        self.numpyData(f'Data1/train/cats', 1)
        self.listXData = np.array(self.listXData)
        np.random.shuffle(self.listXData)
        self.labelData()
        self.listYData = np.array(self.listYData)
        return self.listXData, self.listYData
        
# listX, listY = Get_Data().getData()
# for i in range(10):
#     randomImg = random.randrange(0, 1000)

#     plt.imshow(listX[randomImg])
#     plt.xlabel(listY[randomImg])
#     plt.show()

# cat_dir = 'Data/train/cats'
# dog_dir = 'Data/train/dogs'

# list_dog = []
# list_cat = []
# list_ani = []

# data = []
# x_train = []
# y_train = []
# for filename in os.listdir(cat_dir):
#     file = os.path.join(cat_dir, filename)
#     list_cat.append(file)
#     list_ani.append(file)
    # img = cv2.imread(file)
    # img = cv2.resize(img, (28,28))
    # data.append((img,[0,1]))
    # x_train.append(img)
    # y_train.append([0, 1])

# for filename in os.listdir(dog_dir):
#     file = os.path.join(dog_dir, filename)
#     list_dog.append(file)
#     list_ani.append(file)
    # img = cv2.imread(file)
    # img = cv2.resize(img, (28,28))
    # data.append((img,[1,0]))
    # x_train.append(img)
    # y_train.append([1, 0])

# random.shuffle(list_ani)
# print(list_ani[0])
# print(len(list_ani))

# for file in list_ani:
#     img = cv2.imread(file)
#     img = cv2.resize(img, (28,28))
#     x_train.append(img)
#     if file in list_cat:
#         y_train.append([0, 1])
#     elif file in list_dog:
#         y_train.append([1, 0])

# np.random.shuffle(data)
# data = np.array(data)
# print(data[0])
# x_train = data[:,0]
# y_train = data[:,1]
# x_train = np.array(x_train)
# y_train = np.array(y_train)







