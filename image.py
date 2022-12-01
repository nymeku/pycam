import cv2
from math import sqrt, floor

canva = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'
img = cv2.imread("./zoidberg.jpg",0)
rows,cols=img.shape

newShape = []
print(cols,rows)
file = open("./output.txt")

for i in range(rows):
    tmp = []
    for j in range(cols):
        pixel_b, pixel_g, pixel_r = img[i][j]
        print(pixel_b,pixel_g,pixel_r)



def pick_char(r,g,b):
    brightness = sqrt(r**2 * .241 + g**2 * .691 + b**2 * .068)
    return canva[floor(brightness/255)]

