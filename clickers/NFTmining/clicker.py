import pyautogui
import time


def clicker():
    try:
        while True:
            # Клик левой кнопкой мыши по первой области экрана
            x = 460
            y = 650
            pyautogui.moveTo(x, y)
            time.sleep(1)
            pyautogui.click(button='left')
            #pyautogui.moveRel(50, 50)


            # Ждем 12 секунд
            time.sleep(12)

            # Клик левой кнопкой мыши по второй области экрана
            x = 1515
            y = 555
            pyautogui.moveTo(x, y)
            pyautogui.scroll(-70)
            time.sleep(1)
            pyautogui.click(button='left')
            time.sleep(25)
            pyautogui.scroll(100)
            
    except KeyboardInterrupt:
        print('\nВыход из программы')



if __name__ == '__main__':
    time.sleep(10) # пауза перед запуском функции
    clicker()
