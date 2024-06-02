"""
Скрипт находит совпадения на скриншоте с переданным изображением и визуализирует результат (+ кликает по координатам).
"""

import pyautogui
import cv2
import numpy as np
import pyautogui
import keyboard


def change():
    global work
    work = not work

work = False


def main():
    keyboard.add_hotkey('`', change)
    try:
        while True:
            if work:
                # Загрузить изображение, которое мы хотим найти на экране
                template = cv2.imread('buttonhot.bmp', 0)
                w, h = template.shape[::-1]

                # Сделать скриншот экрана
                screenshot = pyautogui.screenshot()
                screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

                # Перевести скриншот в оттенки серого
                gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)

                # Найти изображение на экране
                result = cv2.matchTemplate(gray_screenshot, template, cv2.TM_CCOEFF_NORMED)
                threshold = 0.8
                loc = np.where(result >= threshold)

                # Получить координаты найденного изображения
                for pt in zip(*loc[::-1]):
                    cv2.rectangle(screenshot, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

                # # Кликнуть по найденным координатам
                # for pt in zip(*loc[::-1]):
                #     center_x = pt[0] + w // 2
                #     center_y = pt[1] + h // 2
                #     pyautogui.click(center_x, center_y)

                # Показать результаты
                cv2.imshow('Detected', screenshot)
                cv2.waitKey(0)  # ожидание нажатия любой клавиши
                cv2.destroyAllWindows()
    
    except KeyboardInterrupt:
        print('\nВыход из программы')


if __name__ == '__main__':
    main()
