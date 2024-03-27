# kerakli kutubxonalar
import numpy as np
import cv2
import face_recognition
import os
from datetime import datetime

img_path = 'ImageTest' # test uchun rasmlar joylashgan fayl
im_list = []
names = []
img_names = os.listdir(img_path)
print(img_names)
# Rasmlarning nomini listga yozib olish
for img in img_names:
    image = cv2.imread(f"{img_path}/{img}")
    im_list.append(image)
    names.append(os.path.splitext(img)[0])
print(names)

# Rasmlarni kodlash , piksellarini aniqlab ularni listga yoziladi
def findencodings(images):
    en_list=[]
    for image in images:
        Image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) #
        encoding = face_recognition.face_encodings(Image)[0] # rasmlarni ortidagi 0 va 1 orasidagi pixellarni oqib oladi
        en_list.append(encoding) # bu  ularning har birini listga joylaydi
    return  en_list
# bu funsiya bizdagi oqitilgan malumotlarga asosan web kameradagi korsatilgan rasm bilan bir xil rasm haqida malumotlarni
# csv faylga yozib boradi
def attendance(names):
    with open("attendances.csv","r+") as fl: # csv faylga classlarni va ularning koringan
        datas = fl.readlines()               # vaqtini joylab boradi
        namelist=[]
        for line in datas:
            new_entry =  line.split(",")
            namelist.append(new_entry[0])
        if names not in namelist: # Agar bir class listda mavjud bo'lsa qayta yozmaydi,yangi classni yozadi
            current = datetime.now()
            dtStr = current.strftime("%H:%M:%S") # vaqtni ham yozib qo'yadi
            fl.writelines(f"\n{names},{dtStr}")

knownFaceEncodings = findencodings(im_list)
print("Encodings Done!")

# Veb kameraga ulanib tekshirish

Webcam = cv2.VideoCapture(0)
print("Loading...")

while True :
    cap,img = Webcam.read()
    #rasmni hajmini kichraytirish dastur tezligini oshiradi
    imgK = cv2.resize(img,(0,0),None,0.25,0.25) # rasmni 1/4 marta kichraytirdik
    imgK = cv2.cvtColor(imgK, cv2.COLOR_BGR2RGB)

    facelocsCFrame = face_recognition.face_locations(imgK) # yuz joylashgan qismni aniqlaydi
    encodedCurrentFrame = face_recognition.face_encodings(imgK,facelocsCFrame)

    for faces,encode in zip(facelocsCFrame,encodedCurrentFrame):
        compare = face_recognition.compare_faces(knownFaceEncodings, encode) # bu yuz piksellarni solishtiadi
        distances = face_recognition.face_distance(knownFaceEncodings, encode) # biz oqitgan malumotlar orasidan eng
        matchedIndex= np.argmin(distances)                                     # kichik oraliq masofaga ega bolgani
                                                                               # web kameradagi rasm bilan bir xil boladi

        if compare[matchedIndex]:
            n = names[matchedIndex].upper() # class nomini katta harfga aylantirib oladi
            y1,x2,y2,x1  = faces # bu yuz joylashgan parametrlar listi
            y1, x2, y2, x1  = y1*4,x2*4,y2*4,x1*4 # rasmni 1/4 marta kichraytib olganimiz uchun o'z xoliga qaytaramiz
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2) # tortburchak chizadi
            cv2.rectangle(img,(x1, y2-35), (x2, y2), (0, 255, 0),cv2.FILLED) # class nomi uchun tortburchak chizadi
            cv2.putText(img,n,(x1+6,y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2) # class nomi yoziladi
            attendance(n) # har bir classni yozamiz

    cv2.imshow("Camera",img) # kameradagi rasmni originalini  ko'rsatadi
    cv2.waitKey(1) # 1 milli sekundda to'xtatib korsatib beradi