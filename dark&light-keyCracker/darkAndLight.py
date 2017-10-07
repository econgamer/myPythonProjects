import pyautogui, time

import tkinter

time.sleep(5)



# pyautogui.moveTo(100, 100, duration=1)
for i in range(0,1000):

    # pyautogui.moveTo(1312, 900, duration=1)
    # pyautogui.click()
    time.sleep(2)
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


    if i < 999 and i >= 100:
        time.sleep(1)
        print(i)
        pyautogui.typewrite('0'+str(i))


    if i < 9999 and i >= 1000:
        time.sleep(1)
        print(i)
        pyautogui.typewrite(str(i))

    i += 1


#holding e > mouse click to password > release e > enter password
