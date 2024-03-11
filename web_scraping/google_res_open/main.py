import  requests, sys, webbrowser, bs4

print('...search...')
res = requests.get('https://www.google.com/search?q=' +
                   'парсинг на python')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a')

num_open = min(5, len(link_elems))
for i in range(num_open):
    url_open = 'https://www.google.com/search?q=' + link_elems[i].get('href')
    print('Открытие ссылки...', url_open)
    webbrowser.open(url_open)
