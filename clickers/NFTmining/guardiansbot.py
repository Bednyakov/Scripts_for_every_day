from random import randint
import pyautogui
import keyboard
import time

work = False
x_pos = 0
y_pos = 0

def mouse_posotion():
    global x_pos
    global y_pos

    x_pos, y_pos = pyautogui.position()
    print(f'X: {x_pos}, Y: {y_pos}', end='\r')  # Обновляем координаты в одной строке


def guardian():
    points = ((1180, 20), (x_pos, y_pos), (1501, 465), (1481, 443), (1300, 383), (1336, 432),(1419, 476), (1520, 468), (1502, 490), (1417, 488), (1419, 476))
    battle_points = ((1338, 425), (1422, 463), (1338, 425), (1471, 462), (1522, 462), (1419, 476), (1497, 480), (1419, 476))

    for x, y in points:
        time.sleep(0.01)
        pyautogui.click(x=x, y=y, button='left')

def change():
    global work
    work = not work

def main():
    keyboard.add_hotkey('`', change)
    keyboard.add_hotkey('=', mouse_posotion)
    try:
        while True:
            if work:
                guardian()

    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()