
import pyautogui,time
time.sleep(5)
f = open("text.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

# import pyautogui as spam
# import time
#
# time.sleep(5)
#
# limit = input("enter a limit message")
# msg = input("enter a message")
#
# i=0
# while i < int(limit):
#     spam.typewrite(msg)
#     spam.press("enter")
#     i +=1
