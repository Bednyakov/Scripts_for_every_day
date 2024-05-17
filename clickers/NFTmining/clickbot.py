from random import randint
import pyautogui
import keyboard
import time


def hamster():
    pyautogui.moveTo(755, 1062)
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(1497, 496)

    for _ in range(5):
        pyautogui.moveRel(randint(1, 5), randint(1, 5))
        for _ in range(90):
            pyautogui.click(button='left')
            time.sleep(0.001)

    pyautogui.moveTo(755, 1062)
    time.sleep(0.1)
    pyautogui.click()

def hotcoin():
    pyautogui.moveTo(802, 1062)
    time.sleep(0.1)
    pyautogui.click()
    pyautogui.moveTo(1755, 837)
    time.sleep(0.1)
    pyautogui.click()

def nftmining():
    pyautogui.moveTo(1251, 220) # vkladka
    time.sleep(0.01)
    pyautogui.click()

    pyautogui.moveTo(1633, 451) # button
    pyautogui.scroll(200)
    time.sleep(0.01)
    pyautogui.click()

    pyautogui.moveTo(1251, 220) # vkladka
    time.sleep(0.01)
    pyautogui.click()

    time.sleep(randint(1, 2))

    pyautogui.moveTo(849, 1058) # MetaMask
    time.sleep(0.01)
    pyautogui.click()

    pyautogui.moveTo(1859, 577) # Metamask window
    time.sleep(0.01)
    pyautogui.scroll(-70)
    pyautogui.click()

def change():
    global work
    work = not work

work = False

def main():
    hamster_time = 0
    hot_time = 0
    keyboard.add_hotkey('`', change)
    try:
        while True:
            if work:
                if hamster_time >= 600:
                    hamster()
                    hamster_time = 0

                if hot_time >= 100:
                    hotcoin()
                    hot_time = 0
                
                nftmining()

                hamster_time += 1
                hot_time += 1
    
    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()



