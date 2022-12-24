
import pyautogui

region = (1528, 781, 1684-1528, 830-781)

def screenshot_image(filename):
  screenshot_image = pyautogui.screenshot(region=region)
  screenshot_image.save(filename)

screenshot_image('angkat-pancing.png')