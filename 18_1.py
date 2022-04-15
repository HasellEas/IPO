from PIL import Image, ImageDraw
import random

path = input("File: ")

mode = int(input("Mode: "))

image = Image.open(path)
photo_element = image.load()

draw_element = ImageDraw.Draw(image)

if mode == 0:
    for __ in range(image.size[0]):
        for ___ in range(image.size[1]):
            a = photo_element[__, ___][0]; b = photo_element[__, ___][1]; c = photo_element[__, ___][2]
            element = (a+b+c) // 3
            draw_element.point((__, ___),(element,element,element))

    image.save(path+"_output0.jpg", "JPEG")
elif mode == 1:
    d = int(input("depth: "))
    for __ in range(image.size[0]):
        for ___ in range(image.size[1]):
            a = photo_element[__, ___][0]; b = photo_element[__, ___][1]; c = photo_element[__, ___][2]
            element = (a+b+c) // 3
            a = element + d * 2; b = element + d; c = element
            if a > 255: a = 255
            if b > 255: b = 255
            if c > 255: c = 255
            draw_element.point((__, ___),(element,element,element))

    image.save(path+"_output1.jpg", "JPEG")
elif mode == 2:
    for __ in range(image.size[0]):
        for ___ in range(image.size[1]):
            a = photo_element[__, ___][0]; b = photo_element[__, ___][1]; c = photo_element[__, ___][2]
            draw_element.point((__, ___),(255-a,255-b,255-c))

    image.save(path+"_output2.jpg", "JPEG")
elif mode == 3:
    pos = int(input("pos: "))
    for __ in range(image.size[0]):
        for ___ in range(image.size[1]):
            random_num = random.randint(-pos, pos)
            a = photo_element[__, ___][0]+ random_num; b = photo_element[__, ___][1]+ random_num; c = photo_element[__, ___][2]+ random_num
            if a < 0: a = 0
            if b < 0: b = 0
            if c < 0: c = 0
            if a > 255: a = 255
            if b > 255: b = 255
            if c > 255: c = 255
            draw_element.point((__, ___),(a,b,c))

    image.save(path+"_output3.jpg", "JPEG")
elif mode == 4:
    pos = int(input("pos: "))
    for __ in range(image.size[0]):
        for ___ in range(image.size[1]):
            a = photo_element[__, ___][0]+ pos; b = photo_element[__, ___][1]+ pos; c = photo_element[__, ___][2]+ pos
            if a < 0: a = 0
            if b < 0: b = 0
            if c < 0: c = 0
            if a > 255: a = 255
            if b > 255: b = 255
            if c > 255: c = 255
            draw_element.point((__, ___),(a,b,c))

    image.save(path+"_output4.jpg", "JPEG")
elif mode == 5:
    pos = int(input("pos: "))
    for __ in range(image.size[0]):
        for ___ in range(image.size[1]):
            a = photo_element[__, ___][0]+ pos; b = photo_element[__, ___][1]+ pos; c = photo_element[__, ___][2]+ pos
            suma = a+b+c
            if suma > (((255+pos) // 2) *3):
                a=b=c = 255
            else:
                a=b=c = 0
            draw_element.point((__, ___),(a,b,c))

    image.save(path+"_output5.jpg", "JPEG")