import pyautogui
import keyboard
import cv2
import numpy as np
import time


def change():
    global work
    work = not work

work = False

def find_and_click(template_path, threshold=0.6, interval=0.0001):
    keyboard.add_hotkey('`', change)

    # Загружаем изображение, которое мы хотим найти на экране. 0- в градациях серого.
    template = cv2.imread(template_path, 0)
    w, h = template.shape[::-1]

    try:
        while True:
            if work:

                # Получаем скриншот экрана.
                screenshot = pyautogui.screenshot()
                screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                # Переводим скриншот в оттенки серого.
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                # Находим изображение на экране.
                result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                loc = np.where(result >= threshold)

                # Кликаем по найденным координатам.
                for pt in zip(*loc[::-1]):
                    center_x = pt[0] + w // 2
                    center_y = pt[1] + h // 2
                    pyautogui.doubleClick(center_x, center_y)
                    break  # объект loc содержит большие массивы, поэтому прерываем после клика по первым координатам.

                # Короткая задержка перед следующим поиском
                time.sleep(interval)
    
    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == "__main__":
    find_and_click('flower.bmp')
