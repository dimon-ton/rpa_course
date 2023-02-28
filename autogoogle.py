from time import sleep
import webbrowser
import pyperclip
import pyautogui as pa
from datetime import datetime

txt = "อุณหภูมิจังหวัดระยอง"
pyperclip.copy(txt)

url = 'https://www.google.com'

webbrowser.open_new(url)
sleep(1)
pa.hotkey('ctrl', 'v')
pa.hotkey('enter')

# set active window to save screenshot
sleep(1)

region = (210,300,728,406)
d_name = datetime.now().strftime("%Y%m%d_%H%M%S")
pa.screenshot('{}_{}.png'.format(d_name, txt), region=region)

sleep(3)
pa.getWindowsWithTitle("ค้นหาด้วย Google")[0].close()






