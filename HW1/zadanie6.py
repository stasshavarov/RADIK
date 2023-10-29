import requests as re
from airium import Airium

data = re.get('https://dog.ceo/api/breeds/image/random').json()

a = Airium()

a('<!DOCTYPE html>')
with a.html('lang=ru'):
    with a.head():
        a.meta(charset='utf-8')
        a.title(_t='Dogs')

    with a.body():
        image_url = data['message']
        with a.div():
            a.img(src=image_url, alt='Dog', width = '800', height = '800')


with open('text_6_otvet_var_14.html', 'w') as file:
    file.write(str(a))