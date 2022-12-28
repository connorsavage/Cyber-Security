# Purpose

The keylogger on_press function records the current time, key name, process name, window title, username, and IP address of the machine. 
These additional pieces of information are written to the worksheet along with the key name and saved to the Excel file. The workbook is then saved to a file called "keylogs.xlsx".
The program enters an infinite loop, waiting for the user to press the Esc key to exit. While the program is running, any keys that are pressed will be logged.

To log mouse events, you can use the pynput.mouse.Listener class in a similar way as the pynput.keyboard.Listener class. The on_click and on_scroll methods can be used to log mouse clicks and scrolls, respectively.
