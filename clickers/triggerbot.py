import pyautogui
import keyboard
import time

# Отключение fail-safe механизма (НЕ РЕКОМЕНДУЕТСЯ, но в R6 без него часто вылетает скрипт.)
pyautogui.FAILSAFE = False


work = False
point = tuple()
index = 0

def mouse_posotion():
    global index
    global point
    x, y = pyautogui.position()
    point = (x, y)
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel((x, y))

    # Вычисление координат центра экрана
    screen_width, screen_height = pyautogui.size()
    center_x = screen_width // 2
    center_y = screen_height // 2

    print(f'''Координаты точки: X: {x}, Y: {y}, color: {color}. Центр экрана X: {center_x} Y: {center_y}''', end='\r')

def change_clicker():
    global work
    work = not work
    if work:
        print('\nКликер включен!')
    else:
        print('\nКликер выключен!')

def clicker(points: list):
    screenshot = pyautogui.screenshot()
    color = screenshot.getpixel(point)
    if color[0] in range(190, 220) and color[1] > 190 and color[2] > 30:  #R6Siege
    # if color[0] in range(200, 255) and 170 > color[1] > 40 and 170 > color[2] > 30:  #CS2
        pyautogui.doubleClick()


def main():
    keyboard.add_hotkey('`', change_clicker)
    keyboard.add_hotkey('=', mouse_posotion)

    try:
        while True:
            if work:
                clicker(point)
            time.sleep(0.001)

    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()
