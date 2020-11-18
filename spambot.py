import pyautogui
import schedule
import time
import random
time.sleep(5)


def job():
    ha = random.choice(list(open('dad.txt')))
    pyautogui.typewrite(ha)
    pyautogui.press("enter")


schedule.every(1).minutes.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
