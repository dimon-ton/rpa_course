import pyperclip
import pyautogui as pa

text = "อุณหภูมิจังหวัดระยอง"
pyperclip.copy(text)

pa.getWindowsWithTitle("New Tab")[0].restore()

# pa.moveTo(duration=5, x=152, y=53)

# pa.click()

# pa.hotkey('ctrl', 'v')
# pa.hotkey('enter')