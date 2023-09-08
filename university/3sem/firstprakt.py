import numpy as np
import cv2


def save(img, kernel_work, name):
    kernel_work = kernel_work / (np.sum(kernel_work) if np.sum(kernel_work) != 0 else 1)
    img_rst = cv2.filter2D(img, -1, kernel_work)
    cv2.imwrite('result_' + str(name + 1) + '.jpg', img_rst)
    hori = np.concatenate((img, img_rst), axis=1)
    scale_percent = 30
    width = int(hori.shape[1] * scale_percent / 100)
    height = int(hori.shape[0] * scale_percent / 100)
    dsize = (width, height)
    output = cv2.resize(hori, dsize)
    cv2.imshow('end', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


kernel_list = [[[1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1],
                   [1, 1, 1, 1, 1]],
               [[0.0, -1.0, 0.0],
                [-1.0, 4.0, -1.0],
                [0.0, -1.0, 0.0]],
               [[0.0, -1.0, 0.0],
                [-1.0, 5.0, -1.0],
                [0.0, -1.0, 0.0]],
                [[-1.0, -1.0],
                 [2.0, 2.0],
                 [-1.0, -1.0]]
               ]

for i in range(4):
    img = cv2.imread(str(i+1) + '.jpg')
    kernel = np.array(kernel_list[i])
    save(img, kernel, i)
img = cv2.imread('test.jpg')
kernel = np.array([[0, -1, 0],
 [-1.0, 3, -1.0],
 [0, -1, 0]])
kernel = kernel/(np.sum(kernel) if np.sum(kernel)!=0 else 1)
img_rst = cv2.filter2D(img, -1, kernel)
hori = np.concatenate((img, img_rst), axis=1)
cv2.imshow('end', hori)
cv2.waitKey(0)
cv2.destroyAllWindows()
