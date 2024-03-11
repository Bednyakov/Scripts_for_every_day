
import re, pyperclip

phone = re.compile(r'''(
(\s|-|\.)*
(\d)
(\s|-|\.)?
(\d{3}|\(\d{3}\))
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{4}|\d{2})
(\s|-|\.)?
(\d{2})?
(\s*(доб|доб.)\s*(\d{2,5}))?
)''', re.VERBOSE)

email = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
list = []

for groups in phone.findall(text):
    phoneNums = '-'.join([groups[2], groups[4], groups[6], groups[8], groups[10]])
    if groups[11] != '':
        phoneNums += ' x' + groups[11]
    list.append(phoneNums)
for groups in email.findall(text):
    list.append(groups[0])

if len(list) > 0:
    pyperclip.copy('\n'.join(list))
    print('Скоипировано в буфер обмена.')
    print('\n'.join(list))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены.')

























