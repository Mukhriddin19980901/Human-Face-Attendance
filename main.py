import numpy as np
import cv2
import face_recognition

ImageJason = face_recognition.load_image_file("ImageMain/jason_statham.jpg")
ImageJason = cv2.cvtColor(ImageJason,cv2.COLOR_BGR2RGB)
ImageJason = cv2.resize(ImageJason,(700,700))

ImgTest = face_recognition.load_image_file("ImageMain/leonardo-dicaprio.jpg")
ImgTest = cv2.cvtColor(ImgTest,cv2.COLOR_BGR2RGB)

# yuzni aniqlash
FaceLoc = face_recognition.face_locations(ImageJason)[0]
encodingJason = face_recognition.face_encodings(ImageJason)[0]
cv2.rectangle(ImageJason,(FaceLoc[3],FaceLoc[0]),(FaceLoc[1],FaceLoc[2]),(0,255,0),2)

# Test uchun yuzni aniqlash
TestLoc = face_recognition.face_locations(ImgTest)[0]
encodeTest = face_recognition.face_encodings(ImgTest)[0]
cv2.rectangle(ImgTest,(TestLoc[3],TestLoc[0]),(TestLoc[1],TestLoc[2]),(0,255,0),2)

final = face_recognition.compare_faces([encodingJason],encodeTest)
FaceDis = face_recognition.face_distance([encodingJason],encodeTest)

# Rasmni ustiga sharh yozamiz
cv2.putText(ImgTest,f"{final} {round(FaceDis[0],2)} " , (60,60) ,cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
print(final)
print(FaceDis)

cv2.imshow("Jason Statham test",ImgTest)
cv2.imshow("Jason Statham",ImageJason)

cv2.waitKey(0)
