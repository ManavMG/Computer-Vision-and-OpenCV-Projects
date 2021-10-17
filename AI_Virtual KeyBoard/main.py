import cv2
#import detector as detector
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import numpy as np
import cvzone
from pynput.keyboard import Controller

cap1 = cv2.VideoCapture(0)  #capture the image from web cam
cap1.set(3, 2000)
cap1.set(4, 1200)
detector = HandDetector(detectionCon=0.8, maxHands=2)

keys = [["Q","W","E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "{", "}"],
        ["A","S","D", "F", "G", "H", "J", "K", "L", ";", ":", " ' "],
        ["Z","X","C", "V", "B", "N", "M", ",", ".", "?", "<", ">", "/"]]

finaltext = ""

keyboard = Controller()

def drawALL(img, buttonlist):

    for button in buttonlist:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, button.text, (x + 13, y + 58), cv2.FONT_HERSHEY_PLAIN,
                    4, (255, 255, 255), 4)
    return img


#def drawALL(img, buttonlist):
#    imgNew = np.zeros_like(img, np.uint8)
#    for button in buttonlist:
#        x, y = button.pos
#        cvzone.cornerRect(imgNew, (button.pos[0], button.pos[1],
#                                                   button.size[0],button.size[0]), 20 ,rt=0)
#        cv2.rectangle(imgNew, button.pos, (x + button.size[0], y + button.size[1]), (0, 0, 255), cv2.FILLED)
#        w, h = button.size
#        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 255), cv2.FILLED)
#        cv2.putText(imgNew, button.text, (x + 25, y + 45), cv2.FONT_HERSHEY_PLAIN,
#                   2, (255, 255, 255), 3)
#
#    out = img.copy()
#    alpha = 0.5
#    mask = imgNew.astype(bool)
#    print(mask.shape)
#    out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
#    return out


class Button():
    def __init__(self, pos, text, size=[75,75]):
        self.pos = pos
        self.text = text
        self.size = size


buttonlist = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonlist.append(Button([85 * j + 35, 100 * i + 50], key))  # or (Button([85*j+35, 100*i+50], key)


while True:
    success, img = cap1.read()
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawALL(img, buttonlist)

    if lmList:
        for button in buttonlist:
            x, y = button.pos
            w,h = button.size

            if x< lmList[8][0] <x+w and y< lmList[8][1] <y+h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 13, y + 58), cv2.FONT_HERSHEY_PLAIN,
                            4, (255, 255, 255), 4)

                l, _, _ = detector.findDistance(8, 12, img,draw=False) #8 is index of first finger and 12 is of middle
                print(l)

                if l<35:
                    keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 13, y + 58), cv2.FONT_HERSHEY_PLAIN,
                                4, (255, 255, 255), 4)
                    finaltext += button.text
                    sleep(0.3)

        cv2.rectangle(img, (50,350), (700,450), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, finaltext, (60,430), cv2.FONT_HERSHEY_PLAIN,
                    4, (255, 255, 255), 4)




    #img = myButton.draw(img)

    cv2.imshow("Image", img) #show that image
    cv2.waitKey(1)