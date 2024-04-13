import pyautogui
import time
import keyboard

def click_alternate(first_x, first_y, second_x, second_y):
    while True:
        if keyboard.is_pressed('q'):  # Нажмите 'q' для выхода из цикла
            break
        pyautogui.click(first_x, first_y)
        time.sleep(0.5)
        pyautogui.click(second_x, second_y)
        time.sleep(0.5)


def get_cursor_position():
    x, y = pyautogui.position()
    return x, y

# Пример использования функции для получения координат курсора
cursor_x, cursor_y = get_cursor_position()
print(f"Координаты курсора мыши: x={cursor_x}, y={cursor_y}")


if __name__ == '__main__':
    first_x, first_y = 100, 100
    second_x, second_y = 500, 100
    click_alternate(first_x, first_y, second_x, second_y)

    # sudo python3 click.py
