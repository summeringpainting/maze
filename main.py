import cv2
import numpy as np
import keyboard
import time

source = cv2.imread("14_generated.jpg", 1)

# grey_source = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# make image smaller
scaleX = 0.3
scaleY = 0.3

scaleDown = cv2.resize(source,
                       None,
                       fx=scaleX,
                       fy=scaleY,
                       interpolation=cv2.INTER_LINEAR)

# make image an array
img_array = np.array(scaleDown)

x = 10
x1 = 20

y = 260
y1 = 270

# Starting point for square
img_array[10:20, 260:270] = .1

black_lines = [2, 2, 2] or [1, 3, 2] or [1, 1, 1]

white = [249, 246, 255]

# Game Loop
while True:
    cv2.imshow('cool maze',
               img_array)

    if (keyboard.is_pressed('s') and
            black_lines not in img_array[x+10:x1+10, y:y1]):
        if x >= 509:
            print("You Win!!!")
            print("You Win!!!")
            print("You Win!!!")
            print("You Win!!!")
            print("You Win!!!")
            time.sleep(3)
            break

        img_array[x:x1, y:y1] = white
        x += 10
        x1 += 10

        img_array[x:x1, y:y1] = .1

        cv2.imshow('cool maze',
                   img_array)

        print(f"pressed s new coords is {x} {x1}")

    elif (keyboard.is_pressed('w') and
            black_lines not in img_array[x-10:x1-10, y:y1]):

        img_array[x:x1, y:y1] = white
        x += -10
        x1 += -10

        img_array[x:x1, y:y1] = .1
        cv2.imshow('cool maze',
                   img_array)
        print(f"pressed w new coords is {x}:{x1}, {y}:{y1}")

    elif (keyboard.is_pressed('d') and
            black_lines not in img_array[x:x1, y+10:y1+10]):

        img_array[x:x1, y:y1] = white
        y += 10
        y1 += 10

        img_array[x:x1, y:y1] = .1
        cv2.imshow('cool maze',
                   img_array)
        print(f"pressed d new coords is {x}:{x1}, {y}:{y1}")

    elif (keyboard.is_pressed('a') and
            black_lines not in img_array[x:x1, y-10:y1-10]):

        img_array[x:x1, y:y1] = white
        y += -10
        y1 += -10

        img_array[x:x1, y:y1] = .1
        cv2.imshow('cool maze',
                   img_array)
        print(f"pressed y new coords is {x}:{x1}, {y}:{y1}")

    elif img_array[x == 510]:
        print("WIN")

    else:
        print("WALL")
    cv2.waitKey(0)

cv2.destroyAllWindows()
