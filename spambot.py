import pyautogui
import schedule
import time
import random
time.sleep(5)


def job():
    ha = random.choice(list(open('dad.txt')))
    pyautogui.typewrite(ha)
    pyautogui.press("enter")


schedule.every(1).minutes.do(job) # This will send a text every 1 minute
schedule.every().day.at("10:30").do(job) # This will send a message at 10:30 am everyday as long as program is running and The chat is kept open

while True:
    schedule.run_pending()
    time.sleep(1)
