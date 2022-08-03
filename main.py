import cv2
import numpy as np
import keyboard

source = cv2.imread("14_generated.jpg", 1)

scaleX = 0.3
scaleY = 0.3

scaleDown = cv2.resize(source,
                       None,
                       fx=scaleX,
                       fy=scaleY,
                       interpolation=cv2.INTER_LINEAR)

img_array = np.array(scaleDown)
x = 10
x1 = 20
img_array[10:20, 260:270] = .1
while True:
    cv2.imshow('cool maze',
               img_array)

    if keyboard.is_pressed('s'):
        img_array[x:x1, 260:270] = 255
        x += 10
        x1 += 10

        img_array[x:x1, 260:270] = .1

        print(f"hi {x} {x1}")

    cv2.waitKey(0)

cv2.destroyAllWindows()
