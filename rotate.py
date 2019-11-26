import imutils
import cv2
import os

def bilddrehen(pathzubild, name):
    image = cv2.imread(pathzubild)
    for angle in [0,90,180,270]:
        rotated = imutils.rotate_bound(image, angle)
        cv2.waitKey(0)
        cv2.imwrite('neu/'+name+'-'+str(angle)+'.jpg', rotated)
        print('Bild ',name, ' um ', angle, '° gedrehet und gespeichert')

for file in os.listdir("images/"):
        bilddrehen('images/'+file, file)