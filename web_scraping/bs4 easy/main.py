import requests, bs4

res = requests.get('https://en.wikipedia.org/wiki/Web_scraping')
res.raise_for_status() # метод остановит программу в случае неудачной загрузки

'''чтобы получить элемент веб-страницы из объекта бс, нужно вызвать метод select(), возвращающий объект Tag,
и передать ему строку CSS-селектора искомого элемента (напоминает регулярные выражения, но в HTML страницах)'''

'''Примеры CSS-селекторов soup.select('селектор'):
div, #author, .notice, div span, div>span, input[name], input[type='button']
!!! Селекторы могут сочетаться, образуя сложные шаблоны (p #author)

Скопировать нужный селектор можно в браузере, в консоли разработчика (правой кнопкой на код элемента -> копировать -> CSS-селектор)'''

with open('file.html', 'wb') as file:
    file.writelines(res) # копируем html страницу целиком

with open('file.html', 'rb') as file:# заново открываем файл в режиме чтения
    bsfile = bs4.BeautifulSoup(file.read(), 'html.parser')#создаем объект бс
    elems = bsfile.select('#mw-content-text > div.mw-parser-output')#возвращаем нужный элемент по селектору (объект Tag)
    # а чтобы извлечь из объекта бс все элементы, в качестве селектора нужно передать 'p'
    print(len(elems))# узнаем количество элементов (1)
    print(elems[0].getText())# распечатываем его
    with open('element.txt', 'w', encoding='utf-8') as element_file:
        element_file.writelines(elems[0].getText())# записываем спарсенное в новый файл



