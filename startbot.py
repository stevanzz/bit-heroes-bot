import time
import win32api
import win32con
import pyautogui

confidence = 0.8
status = [
    "mulai",
    "lempar",
    "angkat",
    "trade",
    "selesai"
]
current_status = "mulai"
time_sleep = 0.1
lempar_counter = 0

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)



while True:
    print(current_status)
    if current_status == 'lempar':
        time_sleep = 0.1

    # mulai
    if current_status == 'mulai' and pyautogui.locateOnScreen('mulai-mancing.png', region=(700, 925, 1225-700, 1035-925), confidence=confidence) != None:
        click(960, 980)
        current_status = status[status.index(current_status) + 1]
        time_sleep = 0.35
    # lempar pancing
    if current_status == 'lempar' and pyautogui.locateOnScreen('lempar-pancing.png', region=(460, 725, 925-460, 900-725), confidence=confidence) != None:
        click(960, 980)
        current_status = status[status.index(current_status) + 1]
        time_sleep = 0
    # angkat pancing
    if current_status == 'angkat' and pyautogui.locateOnScreen('angkat-pancing.png', region=(1500, 765, 1715-1500, 845-765), confidence=confidence) != None:
        click(960, 980)
        current_status = status[status.index(current_status) + 1]
        time_sleep = 0.5
    # kalo dapet misc
    if (current_status == 'angkat'  or current_status == 'trade') and pyautogui.locateOnScreen('trade-misc.png', region=(770, 900, 1150-770, 990-900), confidence=confidence) != None:
        click(960, 945)
        current_status = status[status.index(current_status) + 1]
        time_sleep = 0.5
    # it got away
    if (current_status == 'lempar' or current_status == 'trade') and pyautogui.locateOnScreen('got-away.png', region=(810, 700, 1105-810, 790-700), confidence=confidence) != None:
        click(965, 745)
        current_status = 'mulai'
        time_sleep = 1
    # trade
    # if current_status == 'trade' and pyautogui.locateOnScreen('trade-misc.png', region=(770, 900, 1150-770, 990-900), confidence=confidence) != None:
    #     click(945, 920)
    #     current_status = status[status.index(current_status) + 1]
    #     time_sleep = 0.5
    # selesai
    if current_status == 'selesai' and pyautogui.locateOnScreen('selesai-mancing.png', region=(1290, 260, 1380-1290, 350-260), confidence=confidence) != None:
        click(1335, 305)
        current_status = 'mulai'
        time_sleep = 1


    # semakin kecil interval semakin sering bot akan check screen
    # semakin besar, bot akan lebih jarang check screen (lebih besar kemungkinan gagal)
    # print("sleep")
    time.sleep(time_sleep)

