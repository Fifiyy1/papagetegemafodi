# #OpenCV
# #Встановлення
# #pip install opencv-python
# #Деталі
# #https://opencv.org/
#
# #Виведемо зображення
# import cv2
# image_path = "cat.jpeg"
# image = cv2.imread(image_path)
# cv2.imshow("Cat", image)
# cv2.waitKey()
#
# #Нейронні мережі
# #https://github.com/opencv/opencv/tree/3.4/data/haarcascades

#
# import cv2
# image_path = 'cat.jpeg'
# # #Створимо об’єкт, який працюватиме з зображенням
# cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
# image = cv2.imread(image_path)
# # #Знаходимо та виводимо координати мордочки
# cat_face = cat_face_cascade.detectMultiScale(image)
# print(cat_face)
# cv2.imshow("Cat", image)
# cv2.waitKey()


# import cv2
# image_path = 'cat.jpeg'
# # #Створимо об’єкт, який працюватиме з зображенням
# cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
# image = cv2.imread(image_path)
# # #Знаходимо та виводимо координати мордочки
# cat_face = cat_face_cascade.detectMultiScale(image)
# print(cat_face)
# # #Намалюємо прямокутник навколо об'єкта
# for (x, y, w, h) in cat_face:
#     cv2.rectangle(image, (x, y), (x+w, y+h), (128, 255, 128), 2)
# cv2.imshow("Cat", image)
# cv2.waitKey()


#Pillow - робота з зображеннями
# Встановлення
#pip install pillow

import cv2
from PIL import Image
image_path = 'poworiha.png'
poworiha_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_extended.xml')
image = cv2.imread(image_path)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
poworiha_face = poworiha_face_cascade.detectMultiScale(image, 1.9)
# poworiha_face = poworiha_face_cascade.detectMultiScale(image,
#                                              scaleFactor=1.4,
#                                              minNeighbors=5,
#                                              minSize=(10, 10)
#                                              )
print(poworiha_face)
# #Створимо об’єкти зображень для кота та окулярів
poworiha = Image.open(image_path)
glasses = Image.open('glasses.png')
# #альфа-канал дає змогу зробити маску (використати прозорий фон)
poworiha = poworiha.convert("RGBA")
poworiha.resize((500,500))

glasses = glasses.convert("RGBA")
for (x,y,w,h) in poworiha_face:
# #Підпасуємо розмір окулярів до мордочки
# #зображення прямокутнt, для втримання пропорції поділимо висоту на 3
   glasses = glasses.resize((w, int(h/3)))
# #до y додамо значення h/4, бо висота зображення рівна h/3,
# #а очі кота розташовані вище середини мордочки.
   poworiha_face.paste(glasses, (x, int(y+h/3)),glasses)
   poworiha_face.save("poworiha_w_glasses.png")
   poworiha_w_glasses = cv2.imread("poworiha_w_glasses.png")
   cv2.imshow("poworiha_w_glasses", poworiha_w_glasses)
   cv2.waitKey()
cv2.imshow("poworiha", image)
cv2.waitKey()
