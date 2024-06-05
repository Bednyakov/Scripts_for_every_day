"""
После запуска скрипта необходимо назначить координаты двадцати кликов:
1. Переместить курсор в нужное место.
2. Нажать клавишу '=' (равно). В коносли будут прописаны номер точки и координаты.
Повторить для каждой из 20 позиций кликов.
3. Для запуска кликера нажать тильду (Ё).
4. Остановить кликер - нажать тильду (Ё).
"""

import pyautogui
import keyboard
import time

work = False
points = [(0, 0) for _ in range(20)]
index = 0

def mouse_posotion():
    global index
    x, y = pyautogui.position()
    points[index] = x, y
    print(f'Координаты точки {index + 1}: X: {x}, Y: {y}', end='\r')
    index += 1
    if index > 19:
        index = 0

def change_clicker():
    global work
    work = not work

def clicker(points: list):
    for point in points:
        screenshot = pyautogui.screenshot()
        color = screenshot.getpixel((point[0], point[1]))
        if color[0] in range(134, 218) and color[1] != color[2]:
            pyautogui.click(point[0], point[1])

    time.sleep(0.0001)


def main():
    keyboard.add_hotkey('`', change_clicker)
    keyboard.add_hotkey('=', mouse_posotion)

    try:
        while True:
            if work:
                clicker(points)

    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()
