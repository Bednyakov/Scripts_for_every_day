import webbrowser, sys, pyperclip
# программа открывает карту в браузере, используя почтовый адрес из командной строки
# или буфера обмена

if len(sys.argv) > 1:
    # получение адреса из командной строки (срез без первого элемента)
    address = ''.join(sys.argv[1:])
else:
    # получение адреса из буфера
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
