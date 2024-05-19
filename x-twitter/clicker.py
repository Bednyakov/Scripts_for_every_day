import pyautogui
import keyboard
import time

x_pos = 0
y_pos = 0
work = False

def mouse_posotion():
    global x_pos
    global y_pos

    x_pos, y_pos = pyautogui.position()
    print(f'X: {x_pos}, Y: {y_pos}', end='\r')  # Обновляем координаты в одной строке

def change():
    global work
    work = not work

def del_tweet():
    pyautogui.click()
    time.sleep(0.01)
    pyautogui.press('enter')



def main():
    keyboard.add_hotkey('`', change)
    keyboard.add_hotkey('=', mouse_posotion)
    try:
        while True:
            if work:
                del_tweet()
                pyautogui.scroll(-1)

    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()
