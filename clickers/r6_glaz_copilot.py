import pyautogui
import keyboard
import time

# Отключение fail-safe механизма (НЕ РЕКОМЕНДУЕТСЯ, но в R6 без него часто вылетает скрипт.)
pyautogui.FAILSAFE = False

work = False
trigger = tuple()

def trigger_position() -> None:
    global trigger
    # Вычисление координат центра экрана
    screen_width, screen_height = pyautogui.size()
    x = screen_width // 2
    y = screen_height // 2
    trigger = (x, y-3)

def change_clicker():
    global work
    work = not work
    if work:
        print('Кликер включен!', end='\r')
    else:
        print('Кликер выключен!', end='\r')

def clicker(trigger):
    screenshot = pyautogui.screenshot()
    red, green, blue = screenshot.getpixel(trigger)
    if red in range(190, 220) and green > 190 and blue > 30:
        pyautogui.click()


def main():
    keyboard.add_hotkey('`', change_clicker)

    try:
        while True:
            if work:
                clicker(trigger)
            time.sleep(0.0001)

    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    trigger_position()
    main()
