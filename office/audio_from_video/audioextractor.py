def power(elem, struct):
    if elem in struct:
        return struct[elem]
    else:
        for i in struct:
            power(elem, struct)



site = {

    'html': {

        'head': {

            'title': 'Мой сайт'

        },

        'body': {

            'h2': 'Здесь будет мой заголовок',

            'div': 'Тут, наверное, какой-то блок',

            'p': 'А вот здесь новый абзац'

        }

    }

}

print(power('body', site))