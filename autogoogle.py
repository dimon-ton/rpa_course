from time import sleep
import webbrowser
import pyperclip
import pyautogui as pa

txt = "อุณหภูมิจังหวัดระยอง"
pyperclip.copy(txt)

url = 'https://www.google.com'

webbrowser.open_new(url)
sleep(1)
pa.hotkey('ctrl', 'v')
pa.hotkey('enter')

# set active window to save screenshot
windows = pa.getWindowsWithTitle('Google')

if len(windows) > 0:
    window = windows[0]
    window.activate()
    sleep(1)
    screenshot = window.screenshot
    screenshot.save()
    
else:
    print("Window not found")







