import pyautogui
import time
import pyperclip

from datetime import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5   

print("This is the daily report.")
time.sleep(2)

print("Step 1: Open the Chrome browser.")
time.sleep(2)

pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)
pyautogui.write('chrome')  # Type 'chrome' to open the Chrome browser
time.sleep(1)
pyautogui.press('enter')  # Press Enter to open Chrome
time.sleep(3)  # Wait for Chrome to open


print("Step 2: Go to the website.")
pyautogui.hotkey('ctrl', 'l')  # Focus on the address bar
time.sleep(1)
pyautogui.write('https://indianexpress.com/')  # Type the website URL
time.sleep(1)
pyautogui.press('enter')  # Press Enter to navigate to the website
time.sleep(3)
  # Wait for the website to load

print("Step 3: Copy the full data.")
pyautogui.hotkey('ctrl', 'a')  # Select all text on the page
time.sleep(1)   
pyautogui.hotkey('ctrl', 'c')  # Copy the selected text
time.sleep(1)  # Wait for the copy operation to complete

print("Step 4: Open the excel file .")
pyautogui.hotkey('win', 'r')  # Open the Run dialog
time.sleep(1)   
pyautogui.write('excel')  # Type 'excel' to open the Excel application
time.sleep(1)       

pyautogui.press('enter')  # Press Enter to open Excel
time.sleep(3)  # Wait for Excel to open

pyautogui.hotkey('ctrl', 'v')  # Paste the copied text
time.sleep(3)  # Wait for the paste operation to complete
pyautogui.hotkey('ctrl', 's')  # Save the file
time.sleep(2)
pyautogui.write('daily_report.xlsx')  # Type the filename
time.sleep(5)
pyautogui.press('enter')  # Press Enter to save the file
time.sleep(1)
pyautogui.hotkey('alt', 'f4')  # Close Excel
pyautogui.hotkey('alt', 'f4')  # Close Chrome   
print("Step 5: Done.")
print("Daily report generated successfully.")







