import cv2
import os

for i in range(43):
    img = cv2.imread("map/map{0:03d}.bmp".format(i+1))
    print("map/map{0:03d}.bmp".format(i+1))
    img_resized = cv2.resize(img, (960, 720))
    cv2.imshow(f"map{i}", img_resized)
    os.mkdir("map_720")
    cv2.imwrite(f"map_720/map{i+1}.bmp", img_resized)