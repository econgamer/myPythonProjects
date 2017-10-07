import cv2
import numpy as np
import pyautogui, time

#467

time.sleep(5)

for i in range(467,9999):

    # pyautogui.moveTo(1312, 900, duration=1)
    # pyautogui.click()
    time.sleep(1)
    pyautogui.keyDown('e')
    pyautogui.keyUp('e')
    if i < 10:
        time.sleep(1)
        print(i)
        pyautogui.typewrite('000'+str(i))


    if i < 100 and i >= 10:
        time.sleep(1)
        print(i)
        pyautogui.typewrite('00'+str(i))


    if i < 1000 and i >= 100:
        time.sleep(1)
        print(i)
        pyautogui.typewrite('0'+str(i))


    if i < 10000 and i >= 1000:
        time.sleep(1)
        print(i)
        pyautogui.typewrite(str(i))





    pyautogui.screenshot('screen.png');

    img_rgb = cv2.imread('screen.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    template = cv2.imread('screenbar.png',0)
    w, h = template.shape[::-1]

    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    threshold = .90

    loc = np.where( res >= threshold)

    # print(len(loc[0]))

    if len(loc[0]) > 1:
        print('find')
