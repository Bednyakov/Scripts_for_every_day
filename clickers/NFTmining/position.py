import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        print(f'X: {x}, Y: {y}', end='\r')  # Обновляем координаты в одной строке
except KeyboardInterrupt:
    print('\nВыход из программы')
