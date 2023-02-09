'''
1.Отправить запрос для получения всех категорий

2.Получить 1 шутку по каждой из категорий (16 шт) - всего 16 шуток
'''

import requests


class JokeCategories:

    def __int__(self):
        pass

    def get_new_category_joke(self):
        category_url = 'https://api.chucknorris.io/jokes/categories'
        categories = requests.get(category_url)
        categories_list = categories.text.replace('["', '').replace('"]', '').split('","')
        for i in categories_list:
            url = f'https://api.chucknorris.io/jokes/random?category={i}'
            print(url)
            result = requests.get(url)
            print(f'Статус код: {str(result.status_code)}')
            assert result.status_code == 200
            print('Status code ok')
            result.encoding = 'utf-8'
            print(result.text)
            check = result.json()
            check_cat = check.get('categories')
            assert check_cat == [i]
            print('Category ok')
            check_chuck = check.get('value')
            assert 'Chuck' in check_chuck
            print('This joke is about Chuck Norris')


joke = JokeCategories()
joke.get_new_category_joke()
