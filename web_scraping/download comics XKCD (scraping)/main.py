import requests, os, bs4


def scrapy(url: str, dir_name: str) -> None:
	'''Функция извлекает все комиксы с заданного url и сохраняет в заданную директорию'''

	os.makedirs(dir_name, exist_ok=True)  # второй аргумент не бросает исключение, если директория уже создана

	while not url.endswith("#"):

		print("Страница загружается... ")
		res = requests.get(url)
		res.raise_for_status()
		try:
			soup = bs4.BeautifulSoup(res.text, 'lxml')
		except bs4.FeatureNotFound:
			soup = bs4.BeautifulSoup(res.text, 'html.parser')

		comic_element = soup.select('#comic img')

		if comic_element == []:
			print('Изображение не найдено...')
		else:
			comic_image_url = comic_element[0].get('src')

			print(f'Загружаем изображение {comic_image_url}')
			res = requests.get('http:' + comic_image_url)
			res.raise_for_status()

			file = open(os.path.join('comics XKCD', os.path.basename(comic_image_url)), 'wb')
			for chunk in res.iter_content(10000):
				file.write(chunk)
			file.close()

		prev_link = soup.select('a[rel="prev"]')[0]
		url = 'http://xkcd.com' + prev_link.get('href')

	print('Работа программы завершена.')

if __name__ == '__main__':
	scrapy('http://xkcd.com', 'comics XKCD')


