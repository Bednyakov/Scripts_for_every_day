import easyocr

def image_to_text(file_path: str) -> None:
    '''Находит текст на изображении и записывает в текстовый файл.'''
    reader = easyocr.Reader(['en'])
    result = reader.readtext(file_path)  # 2-th & 3-th args: detail=1, paragraph=True

    with open('new_text.txt', 'w') as file:
        for line in result:
            for item in line:
                if type(item) is str:
                    file.write(f'{item}\n')

if __name__ == '__main__':
    image_to_text('image.jpg')

