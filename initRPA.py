import pyautogui as pa
from time import sleep
import pyperclip

txt = "สวัสดี"
pyperclip.copy(txt)


# pyautogui.getWindowsWithTitle("Finance 2022 - Login - Appsheet")[0].maximize()

pa.moveTo(x=1469, y=60)




pa.tripleClick()


pa.hotkey('ctrl', 'v')

