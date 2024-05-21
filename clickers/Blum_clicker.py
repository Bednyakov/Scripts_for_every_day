"""
После запуска скрипта необходимо назначить координаты шести кликов:
1. Переместить курсор в нужное место.
2. Нажать клавишу '=' (равно).
Повторить для каждой из 6 позиций кликов.
3. Для запуска кликера нажать тильду (Ё).
4. Остановить кликер - нажать тильду (Ё).

Второй режим прокликивает 8 точек вокруг курсора.
Включить его можно клавишей '1'.
"""

import pyautogui
import keyboard
import time

work_clicker = False
work_spam = False
points = [(1237, 197), (1237, 198), (1237, 199), (1239, 197), (1241, 197), (1243, 197)]
index = 0

def mouse_posotion():
    global index
    x, y = pyautogui.position()
    points[index] = x, y
    print(f'Координаты точки {index + 1}: X: {x}, Y: {y}', end='\r')
    index += 1
    if index > 5:
        index = 0

def change_clicker():
    global work_clicker
    work_clicker = not work_clicker

def change_spam_clicker():
    global work_spam
    work_spam = not work_spam


def clicker(points: list):
    for point in points:
        pyautogui.click(point[0], point[1])
    time.sleep(0.0001)

def spam_clicker():
    coordinates = ((10, 0), (0, -10), (-20, 0), (10, 10), (-10, 0), (0, 10), (20, 0), (-10, -10))
    for x, y in coordinates:
        pyautogui.moveRel(x, y)
        pyautogui.click()
    time.sleep(0.00001)

def main():
    keyboard.add_hotkey('`', change_clicker)
    keyboard.add_hotkey('1', change_spam_clicker)
    keyboard.add_hotkey('=', mouse_posotion)

    try:
        while True:
            if work_clicker:
                clicker(points)
            if work_spam:
                spam_clicker()
    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()
