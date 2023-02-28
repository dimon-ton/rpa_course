import pyautogui as pa
from time import sleep
import pyperclip

txt = "สวัสดี"
pyperclip.copy(txt)


# pyautogui.getWindowsWithTitle("Finance 2022 - Login - Appsheet")[0].maximize()

pa.moveTo(x=1200, y=361, duration=3)

pa.click()
pa.write("soup kradukmoo")

