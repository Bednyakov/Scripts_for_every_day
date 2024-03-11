import requests

''' функция requests.get получает строку URL и возвращает объект Response'''

res = requests.get('https://ru.wikipedia.org/wiki/')
print('Объект: ', type(res))
res.raise_for_status() # метод остановит программу в случае неудачной загрузки,
# его можно заключить в блок try/exept, чтобы отработать ошибку без остановки программы
'''
try:
    res.raise_for_status()
exept Exception as exc:
    print('Возникла проблема: %s' % (exc))
'''

if res.status_code == requests.codes.ok: # другой способ проверки успешности выполнения запроса (200 - успех)
    print(f'Статус: {res.status_code}')

print(res.text[:100])# выведем первые 100 символов полученного текста на экран

with open('new_file.txt', 'wb') as file:# аргумент 'wb' необходим для записи бинарных данных
    file.writelines(res)# запишем всё что получили в файл построчно